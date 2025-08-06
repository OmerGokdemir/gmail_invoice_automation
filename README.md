# 📥 Gmail Invoice Automation

Automate the process of downloading PDF invoice attachments from your Gmail account and organizing them into company-specific folders based on the PDF content.

---

## 🚀 Features

- Connects to your Gmail account using the Gmail API with OAuth2 authentication.
- Scans your Gmail inbox (or a specified label) for emails containing PDF attachments.
- Downloads PDF attachments and saves them locally.
- Extracts text from the first page of each PDF to identify the issuing company.
- Automatically organizes invoices into folders named after recognized companies (e.g., Amazon, Hepsiburada, Trendyol, A101, Migros).
- Handles duplicate file names by generating unique file names to avoid overwriting.
- Keeps track of processed emails to prevent duplicate downloads.

---

## ✅ Prerequisites

- Python 3.8 or later
- Google Cloud Platform account with Gmail API enabled
- OAuth 2.0 credentials (`credentials.json`) from Google Cloud Console
- Required Python libraries (listed in `requirements.txt`)

---

## 🖥️ Setup Instructions

### 1. Enable Gmail API and Create OAuth Credentials

- Go to [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the **Gmail API** for your project.
- Navigate to **APIs & Services > Credentials**.
- Create OAuth Client ID credentials:
  - Application type: Desktop app
- Download the `credentials.json` file and place it in your project root directory.

### 2. Install Python Dependencies

Create and activate a Python virtual environment, then install dependencies:

```bash
python -m venv env
source env/bin/activate        # On Linux/macOS
.\env\Scripts\activate         # On Windows PowerShell

pip install -r requirements.txt
```

### 3. Generate OAuth Token

Run the `firstly_token_create.py` script once to authenticate your Gmail account and generate the token.json file:

```bash
python firstly_token_create.py
```

A browser window will open for you to sign in with your Google account and authorize the application.

### 4. Run the Invoice Downloader

Once authenticated, run the main script to fetch and organize your PDF invoices:

```bash
python gmail_invoice_automation.py
```

---

## 🔧 Configuration

*   `INVOICE_LABEL`: Gmail label to scan for emails. Default is `'INBOX'`. Change this if you use custom labels.

*   `SAVE_PATH`: Directory where invoices will be saved (`./Invoices` by default).

*   Recognized companies are identified via keywords in PDF text (adjustable in the regex pattern inside the code).

---

## ⚙️ How It Works

1.  **Authentication:** Uses OAuth 2.0 to securely access your Gmail account.

2.  **Email Listing:** Retrieves email messages from the specified label containing PDF attachments.

3.  **Attachment Download:** Saves each PDF attachment locally.

4.  **PDF Text Extraction:** Reads the first page of the PDF to search for company keywords.

5.  **File Organization:** Moves the saved PDF to a folder named after the identified company.

6.  **Duplicate Handling:** Generates unique filenames if duplicates exist.

7.  **Processed Tracking:** Saves processed email IDs in processed_ids.txt to avoid reprocessing.

---

## 🧪 Troubleshooting & Notes

*   Make sure your Google Cloud project has Gmail API enabled.

*   Ensure `credentials.json` is in the project folder.

*   The script uses `'https://www.googleapis.com/auth/gmail.readonly'` scope for read-only access.

*   If you encounter permission issues, verify that your OAuth consent screen and test users are configured properly in Google Cloud Console.

*   The PDF text extraction depends on the PDF structure; some PDFs may fail extraction.

*   Customize the list of company keywords in the code as needed.

---

## 📁 File Structure

```graphql
.
├── gmail_invoice_automation.py      # Main script
├── firstly_token_create.py          # OAuth token generation script
├── credentials.json                 # Google OAuth client credentials 
                                    # (downloaded from Google Cloud)
├── token.json                      # OAuth access token (created after first run)
├── processed_ids.txt               # List of processed email IDs to prevent duplicates
├── Invoices/                      # Folder where invoices are saved
├── requirements.txt               # Python dependencies
└── README.md                      # This documentation file
```

---

## 🛠️ Dependencies

All required packages are listed in requirements.txt, including:

*   google-auth

*   google-auth-oauthlib

*   google-api-python-client

*   PyPDF2

*   others...

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📩 Contact

For questions, suggestions, or issues, please feel free to contact [me](https://github.com/OmerGokdemir).


****

# 📥 Gmail Fatura Otomasyonu

Bu Python projesi, Gmail hesabınızdan PDF fatura eklerini otomatik olarak indirip, PDF içeriğine göre şirket bazlı klasörlerde organize eder.

## 🚀 Özellikler

-  Gmail API ve OAuth2 kimlik doğrulaması ile Gmail hesabınıza bağlanır

-  Gelen kutunuzu (veya belirtilen bir etiketi) tarayarak PDF ekleri içeren e-postaları bulur

-  PDF eklerini indirip yerel olarak kaydeder

-  Her PDF’nin ilk sayfasındaki metni okuyarak fatura kesen şirketi tanımlar

-  Tanınan şirket isimlerine göre (örneğin Amazon, Hepsiburada, Trendyol, A101, Migros) klasörlere yerleştirir

-  Aynı dosya adları varsa üzerine yazmamak için benzersiz dosya adları üretir

-  İşlenmiş e-postaları takip eder, böylece aynı dosyaları tekrar indirmez

---

##  ✅ Gereksinimler

-  Python 3.8 veya üzeri

-  Gmail API etkinleştirilmiş bir Google Cloud Platform hesabı

-  OAuth 2.0 kimlik bilgisi dosyası (credentials.json)

-  Gerekli Python kütüphaneleri (requirements.txt içinde listelenmiştir)

## 🖥️ Kurulum Adımları

###  1. Gmail API’yi Etkinleştir ve OAuth Kimlik Bilgisi Oluştur

-  [Google Cloud Console](https://console.cloud.google.com/) adresine git.

-  Yeni bir proje oluştur ya da mevcut bir projeyi seç

-  Projeye **Gmail API**’yi etkinleştir

-  **API’ler ve Hizmetler > Kimlik Bilgileri** menüsüne git

-  OAuth istemci kimliği oluştur:

    -  Uygulama türü: Masaüstü uygulaması

-  `credentials.json` dosyasını indir ve proje klasörüne yerleştir

### 2. Python Bağımlılıklarını Yükle

Sanal ortam oluşturup etkinleştir ve bağımlılıkları yükle:

```bash
python -m venv env
source env/bin/activate        # Linux/macOS
.\env\Scripts\activate         # Windows PowerShell

pip install -r requirements.txt
```

### 3. OAuth Token Oluştur

Gmail hesabınızın kimliğini doğrulamak ve token.json dosyasını oluşturmak için `firstly_token_create.py` betiğini bir kez çalıştırın::

```bash
python firstly_token_create.py
```

Bir tarayıcı penceresi açılacak ve Google hesabınızla oturum açmanız istenecek.

### 4. Fatura İndirme Scriptini Çalıştır

Kimliğiniz doğrulandıktan sonra, PDF faturalarınızı almak ve düzenlemek için ana komut dosyasını çalıştırın:

```bash
python gmail_invoice_automation.py
```

****

## 🔧 Yapılandırma

-  `INVOICE_LABEL`: E-postalar için taranacak Gmail etiketi. Varsayılan değer `'INBOX'` şeklindedir. Özel etiketler kullanıyorsanız bunu değiştirin.

-  `SAVE_PATH`: Faturaların kaydedileceği klasör (`./Invoices` varsayılan olarak)

-  Şirket adları, PDF metninde anahtar kelimeler aracılığıyla belirlenir (kod içindeki regex ile ayarlanabilir)

****

## ⚙️ Nasıl Çalışır?

1.  **Kimlik Doğrulama:** OAuth 2.0 ile Gmail hesabınıza güvenli erişim sağlar

2.  **E-posta Listeleme:** Belirtilen etiketteki PDF içeren e-postaları listeler

3.  **Ek İndirme:** Her PDF eklentisini yerel diske kaydeder

4.  **PDF Metin Çıkarımı:** PDF'nin ilk sayfasından şirket adı gibi verileri çıkartır

5.  **Dosya Organizasyonu:** PDF dosyalarını şirket ismine göre klasörlere taşır

6.  **Çakışma Önleme:** Aynı dosya ismi varsa otomatik olarak yeni bir isim verir

7.  **Tekrar İşleme Önleme:** processed_ids.txt dosyasına işlenmiş e-posta kimliklerini kaydeder

****

##  🧪 Sorun Giderme ve Notlar

-  Gmail API’nin etkinleştirildiğinden emin olun

-  `credentials.json` dosyasının proje klasöründe bulunduğuna emin olun

-  Script, yalnızca okuma erişimi için `'https://www.googleapis.com/auth/gmail.readonly'` kapsamını kullanır

-  Yetki hatası alırsanız, Google Cloud Console üzerinden OAuth izin ekranını ve test kullanıcılarını doğru yapılandırdığınızdan emin olun

-  PDF metin çıkarımı, PDF yapısına bağlıdır; bazı belgeler hatalı çıkabilir

-  Şirket anahtar kelimelerini kendi ihtiyaçlarınıza göre kodda güncelleyebilirsiniz

****

##  📁 Proje Dosya Yapısı

```graphql
.
├── gmail_invoice_automation.py      # Ana script
├── firstly_token_create.py          # OAuth token oluşturma scripti
├── credentials.json                 # Google OAuth istemci kimlik dosyası
├── token.json                       # OAuth erişim token'ı (ilk çalıştırmadan sonra oluşur)
├── processed_ids.txt                # İşlenmiş e-posta kimlikleri
├── Invoices/                        # Faturaların kaydedildiği klasör
├── requirements.txt                 # Gerekli Python kütüphaneleri
└── README.md                        # Bu dökümantasyon dosyası
```

****

##  🛠️ Bağımlılıklar

requirements.txt içinde yer alan başlıca kütüphaneler:

-  google-auth

-  google-auth-oauthlib

-  google-api-python-client

-  PyPDF2

-  ve diğerleri...

****

📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır. Dilediğiniz gibi kullanabilir ve değiştirebilirsiniz.

📩 İletişim

Sorularınız, önerileriniz veya katkılarınız için lütfen [benimle](https://github.com/OmerGokdemir) iletişime geçin.
