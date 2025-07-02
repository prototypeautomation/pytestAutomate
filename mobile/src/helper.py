import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder


def openDriver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "FQNBO7LRIVEEJJLB")
    options.set_capability("appPackage", "id.edot.ework.debug")
    options.set_capability("appActivity", "id.edot.onboarding.ui.splash.SplashScreenActivity")
    options.set_capability("noReset", True)
    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver

def getElements(driver):
    return {
        "imgLogo": lambda: driver.find_element("id", "id.edot.ework.debug:id/img_ework"),
        "btnLogin": lambda: driver.find_element("id", "id.edot.ework.debug:id/button_text"),
        "txtIdCompany": lambda: driver.find_element("id", "id.edot.ework.debug:id/tv_company_id"),
        "txtNamaPengguna": lambda: driver.find_element("id", "id.edot.ework.debug:id/tv_username"),
        "txtKataSandi": lambda: driver.find_element("id", "id.edot.ework.debug:id/tv_password"),
        "txtGagalLogin": lambda: driver.find_element("id", "id.edot.ework.debug:id/textView"),
        "btnClose" : lambda: driver.find_element("id", "id.edot.ework.debug:id/btn_x"),
        "btnMenu": lambda: driver.find_element("id", "id.edot.ework.debug:id/imgDrawer"),
        "btnLogout" : lambda: driver.find_element("id", "id.edot.ework.debug:id/nav_logout"),
        "txtSubTittleLogin" : lambda: driver.find_element("id", "id.edot.ework.debug:id/text_sub_title"),
        "btnPelangganBaru": lambda: driver.find_element("xpath", "//android.widget.TextView[@text='Pelanggan Baru']"),
        "btnRegisterPelanggan": lambda: driver.find_element("id", "id.edot.ework.debug:id/tvRegister"),
        "txtNamaOutlet":  lambda: driver.find_element("id", "id.edot.ework.debug:id/et_outlet_name"),
        "txtTlephoneOutlet": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_outlet_phone"),
        "txtEmailOutlet": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_outlet_email"),
        "txtPersonalKontak": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_contact_person"),
        "btnLanjutkan": lambda: driver.find_element("id", "id.edot.ework.debug:id/button_text"),
        "dropdownTypeSaluran": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_channel"),
        "optionTypeSaluran": lambda: driver.find_element("id", "id.edot.ework.debug:id/tvName"),
        "dropdownTypeOutlet": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_outlet_type"),
        "optionTypeOutlet": lambda: driver.find_element("xpath", "//android.widget.TextView[@text='Grosir']"),
        "dropdownDaftarHarga": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_pricelist"),

        "dropdownJenisAlamat": lambda: driver.find_element("id", "id.edot.ework.debug:id/et_address_type"),
        "optionInvoiceAddress": lambda: driver.find_element("xpath", "//android.widget.TextView[@text='Invoice Address']"),
        "txtAddress": lambda: driver.find_element("id", "id.edot.ework.debug:id/etAddress"),
        "dropdownPilihNegara": lambda: driver.find_element("xpath", "//android.widget.EditText[@hint='Pilih Negara']"),
        "optionMalaka": lambda: driver.find_element("xpath", "//android.widget.TextView[@text='Melaka']"),
        "btnTerapkan": lambda: driver.find_element("xpath", "//android.widget.Button[@text='Terapkan']"),
        "dropdownKota": lambda: driver.find_element("xpath", "//android.widget.EditText[@hint='Pilih Kota']"),
        "dropdownLokasi": lambda: driver.find_element("xpath", "//android.widget.EditText[@hint='Pilih Lokasi']"),
        "optionJalanGereja": lambda: driver.find_element("xpath", "//android.widget.TextView[@text='Jalan Gereja']"),
        "dropdownKodePos": lambda: driver.find_element("xpath", "//android.widget.EditText[@hint='Pilih Kode pos']"),
        "optionKodePos": lambda: driver.find_element("id", "id.edot.ework.debug:id/txt_name"),
        "btnLanjutkan2": lambda: driver.find_element("xpath", "//android.widget.Button[@text='Lanjutkan']"),
        "btnTambahDocument": lambda: driver.find_element("id", "id.edot.ework.debug:id/tvAddDocument"),
        "txtNamaDokumen": lambda: driver.find_element("id", "id.edot.ework.debug:id/etName"),
        "txtNomorDokumen": lambda: driver.find_element("id", "id.edot.ework.debug:id/etNumber"),
        "btnUnggahBerkas": lambda: driver.find_element("xpath", "//android.widget.Button[@text='Unggah Berkas']"),
        "btnCapture": lambda: driver.find_element("id", "id.edot.ework.debug:id/btn_capture"),
        "btnPilih": lambda: driver.find_element("id", "id.edot.ework.debug:id/button_text"),
        "btnDaftar": lambda: driver.find_element("xpath", "//android.widget.Button[@text='Daftar']"),
        "btnYa": lambda: driver.find_element("xpath", "//android.widget.Button[@text='Ya']"),


        

        


        





    }

def typeACharacter(indentifier, text):
    indentifier.clear()
    indentifier.send_keys(text)

def swipe(driver, text):
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().className("android.widget.ScrollView")).scrollIntoView(new UiSelector().textContains("{text}"))')

def swipeDown(driver,x, y, duration=800):
    size = driver.get_window_size()
    start_x = size["width"] // 2
    start_y = int(size["height"] * x)
    end_y = int(size["height"] * y)
    driver.swipe(start_x, start_y, start_x, end_y, duration)

