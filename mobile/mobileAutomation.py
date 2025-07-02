from src.helper import openDriver, getElements, typeACharacter, swipe, swipeDown
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from faker import Faker

load_dotenv()
generate = Faker("id_ID")
dataSet = {
    "idCompany": "5102552",
    "namaOutlet": "Toko " + generate.word().capitalize() + " " + generate.city(),
    "teleponOutlet": "81" + generate.numerify(text="##########"),
    "emailOutlet": generate.company_email(),
    "personalKontak": generate.name(),
    "address": generate.address().replace("\n", " ")[:50],
    "NamaDokument": "Nomor Induk Berusaha",
    "nomorDokument": "NIB-" + generate.numerify(text="#####"),
}

def test_TC002_Login_Fail_Using_Wrong_Password():
    driver = openDriver()
    try:
        elements = getElements(driver)
        typeACharacter(elements["txtIdCompany"](), dataSet["idCompany"])
        typeACharacter(elements["txtNamaPengguna"](), os.getenv("USERNAMEMOBILE1"))
        typeACharacter(elements["txtKataSandi"](), os.getenv("WRONGPASSWORDMOBILE"))
        elements["btnLogin"]().click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id.edot.ework.debug:id/cl_header"))
        )
        txtGagalLogin = elements["txtGagalLogin"]().text
        elements["btnClose"]().click()
        assert txtGagalLogin == "Tidak dapat login. Silakan hubungi Sales Admin."

    finally:
        driver.quit()

def test_TC003_Login_Fail_Using_User_Not_Registered_In_Group():
    driver = openDriver()
    try:
        elements = getElements(driver)
        typeACharacter(elements["txtIdCompany"](), dataSet["idCompany"])
        typeACharacter(elements["txtNamaPengguna"](), os.getenv("USERNAMEMOBILE2"))
        typeACharacter(elements["txtKataSandi"](), os.getenv("PASSWORDMOBILE"))
        elements["btnLogin"]().click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id.edot.ework.debug:id/cl_header"))
        )
        txtGagalLogin = elements["txtGagalLogin"]().text
        elements["btnClose"]().click()
        assert txtGagalLogin == "Tidak dapat login. Silakan hubungi Sales Admin."

    finally:
        driver.quit()

def test_TC004_Login_Fail_Using_Inactive_User():
    driver = openDriver()
    try:
        elements = getElements(driver)
        typeACharacter(elements["txtIdCompany"](), dataSet["idCompany"])
        typeACharacter(elements["txtNamaPengguna"](), os.getenv("USERNAMEMOBILE3"))
        typeACharacter(elements["txtKataSandi"](), os.getenv("PASSWORDMOBILE"))
        elements["btnLogin"]().click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id.edot.ework.debug:id/cl_header"))
        )
        txtGagalLogin = elements["txtGagalLogin"]().text
        elements["btnClose"]().click()
        assert txtGagalLogin == "Tidak dapat login. Silakan hubungi Sales Admin."

    finally:
        driver.quit()


def test_TC001_Login_Success():
    driver = openDriver()
    try:
        elements = getElements(driver)
        typeACharacter(elements["txtIdCompany"](), dataSet["idCompany"])
        typeACharacter(elements["txtNamaPengguna"](), os.getenv("USERNAMEMOBILE1"))
        typeACharacter(elements["txtKataSandi"](), os.getenv("PASSWORDMOBILE"))
        elements["btnLogin"]().click()
        assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "id.edot.ework.debug:id/img_ework")))
        elements["btnMenu"]().click()
        elements["btnLogout"]().click()
    finally:
        driver.quit()

def test_TC005_Create_New_Customer_And_Veryfy_Data():
    driver = openDriver()
    try:
        elements = getElements(driver)
        typeACharacter(elements["txtIdCompany"](), dataSet["idCompany"])
        typeACharacter(elements["txtNamaPengguna"](), os.getenv("USERNAMEMOBILE1"))
        typeACharacter(elements["txtKataSandi"](), os.getenv("PASSWORDMOBILE"))
        elements["btnLogin"]().click()
        elements["btnPelangganBaru"]().click()
        elements["btnRegisterPelanggan"]().click()
        typeACharacter(elements["txtNamaOutlet"](), dataSet["namaOutlet"])
        typeACharacter(elements["txtTlephoneOutlet"](), dataSet["teleponOutlet"])
        typeACharacter(elements["txtEmailOutlet"](), dataSet["emailOutlet"])
        typeACharacter(elements["txtPersonalKontak"](), dataSet["personalKontak"])
        swipe(driver, "Daftar Harga")
        elements["dropdownTypeSaluran"]().click()
        elements["optionTypeSaluran"]().click()
        elements["dropdownTypeOutlet"]().click()
        elements["optionTypeOutlet"]().click()
        elements["btnLanjutkan"]().click()
        elements["dropdownJenisAlamat"]().click()
        elements["optionInvoiceAddress"]().click()
        swipe(driver, "Alamat")
        swipe(driver, "Kode pos")
        typeACharacter(elements["txtAddress"](), dataSet["address"])
        elements["dropdownPilihNegara"]().click()
        elements["optionMalaka"]().click()
        elements["dropdownKota"]().click()
        elements["optionMalaka"]().click()
        elements["dropdownLokasi"]().click()
        elements["optionJalanGereja"]().click()
        elements["dropdownKodePos"]().click()
        elements["optionKodePos"]().click()
        elements["btnLanjutkan2"]().click()
        elements["btnTambahDocument"]().click()
        typeACharacter(elements["txtNamaDokumen"](), dataSet["NamaDokument"])
        typeACharacter(elements["txtNomorDokumen"](), dataSet["nomorDokument"])
        elements["btnUnggahBerkas"]().click()
        elements["btnCapture"]().click()
        elements["btnPilih"]().click()
        elements["btnDaftar"]().click()
        elements["btnYa"]().click()
        itteration = 10
        for _ in range(itteration):
            try:
                element = driver.find_element("xpath", f'//android.widget.TextView[@text="{dataSet["namaOutlet"]}"]')
                if element.text == dataSet["namaOutlet"]:
                    assert element.text == dataSet["namaOutlet"]
                    status = True
                    break
            except:
                swipeDown(driver, 0.8, 0.4, 1000)

        element = driver.find_element("xpath", f'//android.widget.TextView[@text="{dataSet["address"]}"]')
        assert element.text == dataSet["address"]

    finally:
        driver.quit()
