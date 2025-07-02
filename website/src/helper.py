import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

timeEveryStep = 1

def clickElement(driver, xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()
    time.sleep(timeEveryStep)

def getText(driver, xpath):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    tag = element.tag_name.lower()
    if tag == "input" or tag == "textarea":
        return element.get_attribute("value").strip()
    else:
        return element.text.strip()

def getValueOnOption(driver, value):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//button/span[contains(text(), '{value}')]"))
    )
    return element.text

def typeACharacter(driver, xpath, text):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.clear()
    element.send_keys(text)
    time.sleep(timeEveryStep)

def waitingAnElement(driver, xpath):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    time.sleep(timeEveryStep)

def scrollElement(driver, xpath, coordinate):
    driver.execute_script(f"arguments[0].scrollTop += {coordinate};", 
    driver.find_element(By.XPATH, xpath))
    time.sleep(timeEveryStep)

def openDriver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver
    
def searchOnList(driver, xpath, companyName):
    getAllDiv = driver.find_elements(By.XPATH, xpath)
    for index, div in enumerate(getAllDiv, start=1):
        if companyName in div.text:
            return index
            break


def getElementsWebsite(driver):
    return {
        "btnEmail": '//button[contains(text(), "Use Email or Username")]',
        "txtEmail": '//input[contains(@name, "username")]',
        "btnLogin": '//button[contains(text(), "Log In")]',
        "txtPassword": '//input[contains(@name, "password")]',
        "txtWelcome": '//span[contains(text(), "Welcome Back,")]',
        "linkCompany": '//a[contains(text(), "Companies")]',
        "btnAddNewCompany": '//button[contains(text(), "+ ")]',

        "txtCompanyName": '//input[contains(@placeholder, "Input Company Name")]',
        "txtInputEmail": '//input[contains(@placeholder, "Input Email")]',
        "txtInputPhone": '//input[contains(@placeholder, "Input Phone")]',
        "txtInputPhoneNumber": '//input[contains(@placeholder, "Input Mobile Number")]',
        "dropDownIndsutryType": '//span[contains(text(), "Choose Industry Type")]',
        "optionIndustryType": '//div[contains(@data-value, "construction")]',
        "dropDownCompanyType": '//span[contains(text(), "Choose Company Type")]',
        "optionCompanyType": '//div[contains(@data-value, "retailer")]',
        "dropDownLanguage": '//span[contains(text(), "Choose Language")]',
        "optionLanguage": '//div[contains(@data-value, "indonesia")]',
        "txtAddress": '//input[contains(@placeholder, "Input Address")]',
        "txtCompanyAddress": '//textarea[contains(@placeholder, "Input Company Address")]',
        "dropDownCountry": '//span[contains(text(), "Choose Country")]',
        "optionCountry": '//div[contains(@data-value, "id")]',
        "dropDownProvince": '//span[contains(text(), "Choose Province")]',
        "optionProvince": '//div[contains(@data-value, "v31")]',
        "dropDownCity": '//span[contains(text(), "Choose City")]',
        "optionCity": '//div[contains(@data-value, "v3171")]',
        "dropDownDistrict": '//span[contains(text(), "Choose District")]',
        "optionDistrict": '//div[contains(@data-value, "v317401")]',
        "dropDownSubDistrict": '//span[contains(text(), "Choose Sub District")]',
        "optionSubDistrict": '//div[contains(@data-value, "manggarai")]',
        "scrollView" : '//div[@id="list-combobox"]',

        "btnNext": '//button[contains(text(), "Next")]',
        "txtBranchName": '//input[contains(@placeholder, "Input Branch Name")]',
        "btnFillSameData": '//button[contains(text(), "Fill in with the same data from the Company records")]',
        "btnCheckTnC": '//button[contains(@role, "checkbox")]',
        "btnRegister": '//button[contains(text(), "Register")]',
        "listOfCompany": '//div[contains(@class, "text-lg font-bold")]',
        "txtNotification": '//p[contains(text(), "Incorrect password")]'

    }