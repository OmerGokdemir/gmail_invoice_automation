import os
import base64
import re
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email import message_from_bytes
from pathlib import Path
from email import header
from PyPDF2 import PdfReader

# CONFIGURATION
INVOICE_LABEL = 'INBOX'  # or if you have a custom Gmail label, its name
SAVE_PATH = Path("./Invoices")
PROCESSED_IDS_FILE = "processed_ids.txt"

if not os.path.exists(PROCESSED_IDS_FILE):
    open(PROCESSED_IDS_FILE, "w").close()

# Gmail API Authentication
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('gmail', 'v1', credentials=creds)

# Read previously processed emails
if os.path.exists(PROCESSED_IDS_FILE):
    with open(PROCESSED_IDS_FILE, 'r') as f:
        processed_ids = set(line.strip() for line in f)
else:
    processed_ids = set()

SAVE_PATH.mkdir(parents=True, exist_ok=True)

def extract_pdf_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        return first_page.extract_text()
    except Exception as e:
        print(f"PDF text could not be extracted: {e}")
        return ""

def clean_filename(filename):
    # Dosya adını decode et
    decoded_parts = header.decode_header(filename)
    decoded_filename = ''.join(
        part.decode(charset or 'utf-8') if isinstance(part, bytes) else part
        for part, charset in decoded_parts
    )
    # Windows'ta geçersiz karakterleri kaldır
    return re.sub(r'[\\/*?:"<>|]', '', decoded_filename)

def get_unique_path(path: Path) -> Path:
    counter = 1
    new_path = path
    while new_path.exists():
        new_path = path.with_name(f"{path.stem} ({counter}){path.suffix}")
        counter += 1
    return new_path

def save_attachment(msg, msg_id):
    for part in msg.walk():
        content_type = part.get_content_type()
        if 'application/pdf' in content_type:
            filename = part.get_filename()
            if not filename:
                filename = f"invoice_{msg_id}.pdf"
            else:
                filename = clean_filename(filename)
            data = part.get_payload(decode=True)

            temp_path = SAVE_PATH / filename
            with open(temp_path, 'wb') as f:
                f.write(data)

            pdf_text = extract_pdf_text(temp_path)
            match = re.search(r"(Amazon|Hepsiburada|Trendyol|A101|Migros)", pdf_text, re.I)
            company = match.group(0) if match else "Unknown"
            company_folder = SAVE_PATH / company.capitalize()
            company_folder.mkdir(exist_ok=True)
            new_path = company_folder / filename
            
            # Create unique name if file already exists
            new_path = get_unique_path(new_path)
            
            temp_path.rename(new_path)
            print(f"Saved to: {new_path}")
            return

def fetch_invoices():
    try:
        results = service.users().messages().list(userId='me', labelIds=[INVOICE_LABEL], q="has:attachment filename:pdf").execute()
        messages = results.get('messages', [])

        print(f"{len(messages)} messages with PDF attachments were found.")

        for message in messages:
            msg_id = message['id']
            if msg_id in processed_ids:
                continue

            msg = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()
            raw_data = base64.urlsafe_b64decode(msg['raw'])
            mime_msg = message_from_bytes(raw_data)
            save_attachment(mime_msg, msg_id)

            # Save processed message ID
            with open(PROCESSED_IDS_FILE, 'a') as f:
                f.write(f"{msg_id}\n")
            processed_ids.add(msg_id)
            time.sleep(1)

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    fetch_invoices()
