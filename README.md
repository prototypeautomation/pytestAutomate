# 📱 Mobile and Website Automation Testing with Selenium, Appium & Pytest

Proyek ini adalah script automation test untuk aplikasi Android eWork menggunakan **Appium v2**, **Selenium**, dan **Pytest**. Tes ini untuk menguji alur pendaftaran pelanggan baru pada aplikasi mobile.

---

## 📦 Tech Stack

- Python 3.10+
- Appium Server v2
- Appium-Python-Client
- Selenium 4
- Pytest
- Faker (untuk data dummy)

---

## 🚀 Instalasi

### 1. Clone repositori

```bash
git clone https://github.com/username/namaprojek.git
cd pytestAutomate
```

### 2. Buat dan Aktivasi Virtual Environtment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Appium dan pastikan adb devices terhubung dengan real device

```bash
adb devices
```

catatan : jika status adb nya unauthorize, di allow dulu bagian USB Debugging di handphone dan pastikan mode pengembang sudah aktif

jika sudah aktif adb nya, lalu jalankan perintah berikut :

```bash
ANDROID_HOME=$HOME/Library/Android/sdk ANDROID_SDK_ROOT=$HOME/Library/Android/sdk appium
```

### 5. Install aplikasi via adb installer

```bash
cd pytestAutomate
adb install ework 1.20.5.apk
```

catatan : device android harus sudah terkoneksi dengan laptop sebagai USB Debugging.

### 6. Cara Menjalankan Tes

1. Pastikan Appium Server v2 sudah berjalan di port default 4723.
2. Hubungkan real device atau emulator Android.
3. Jalankan perintah berikut :

```bash
# untuk Aplikasi mobile
cd mobile
pytest -s -v mobileAutomation.py
```

```bash
# untuk Aplikasi website
cd website
pytest -s -v websiteAutomation.py
```

### 7. Mengatur Test suites atau urutan schenario test

1. Buka Folder website/mobile
2. Buka File conftest.py
3. lalu ubah urutan order seperti berikut :

```bash
# untuk Aplikasi website
def pytest_collection_modifyitems(items):
    order = {
        "test_TC001_Login_Success": 1, # urutan Pertama
        "test_TC002_Login_Fail": 2, # urutan Kedua
        "test_TC003_Add_New_Company": 3, # urutan Ketiga
        "test_TC004_Validate_New_Company": 4 # urutan Pertama
    }
    items.sort(key=lambda item: order.get(item.name, 100))
```

```bash
# untuk Aplikasi mobile
def pytest_collection_modifyitems(items):
    order = {
        "test_TC001_Login_Success": 1, # urutan Pertama
        "test_TC002_Login_Fail_Using_Wrong_Password": 2,  # urutan Kedua
        "test_TC003_Login_Fail_Using_User_Not_Registered_In_Group": 3,  # urutan Ketiga
        "test_TC004_Login_Fail_Using_Inactive_User": 4,  # urutan Keempat
        "test_TC005_Create_New_Customer_And_Veryfy_Data": 5  # urutan Kelima
    }
    items.sort(key=lambda item: order.get(item.name, 100))
```
