import pytest
import time
from dotenv import load_dotenv
import os
from faker import Faker
from src.helper import openDriver, getElementsWebsite, clickElement, typeACharacter, waitingAnElement, scrollElement, searchOnList, getText, getValueOnOption
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

generate = Faker("id_ID")
dataSet = {
    "companyName": generate.company(),
    "companyEmail": generate.company_email(),
    "companyPhone": "81" + generate.numerify(text="#########"),
    "address": generate.address().replace("\n", " ")[:50],
    "branchName": "Headquarter",
    "industryType": "Construction",
    "companyType": "Retailer",
    "country": "Indonesia",
    "province": "DKI JAKARTA",
    "city": "JAKARTA SELATAN",
    "district": "TEBET",
}

load_dotenv()

def test_TC001_Login_Success():
    driver = openDriver()
    try:
        el = getElementsWebsite(driver)
        wait = WebDriverWait(driver, 10)
        driver.get(os.getenv("BASEURL"))
        clickElement(driver, el["btnEmail"])
        typeACharacter(driver, el["txtEmail"], os.getenv("USERNAME") )
        clickElement(driver, el["btnLogin"])
        typeACharacter(driver, el["txtPassword"], os.getenv("PASSWORD"))
        clickElement(driver, el["btnLogin"])
        waitingAnElement(driver, el["txtWelcome"])
        assert getText(driver, el["txtWelcome"]) == "Welcome Back,"
    finally:
        driver.quit()

def test_TC002_Login_Fail():
    driver = openDriver()
    try:
        el = getElementsWebsite(driver)
        wait = WebDriverWait(driver, 10)
        driver.get(os.getenv("BASEURL"))
        clickElement(driver, el["btnEmail"])
        typeACharacter(driver, el["txtEmail"], os.getenv("USERNAME") )
        clickElement(driver, el["btnLogin"])
        typeACharacter(driver, el["txtPassword"], os.getenv("WRONGPASSWORDMOBILE"))
        clickElement(driver, el["btnLogin"])
        waitingAnElement(driver, el["txtNotification"])
        assert getText(driver, el["txtNotification"]) == "Incorrect password"
    finally:
        driver.quit()

def test_TC003_Add_New_Company():
    driver = openDriver()
    try:
        el = getElementsWebsite(driver)
        wait = WebDriverWait(driver, 10)
        driver.get(os.getenv("BASEURL"))
        clickElement(driver, el["btnEmail"])
        typeACharacter(driver, el["txtEmail"], os.getenv("USERNAME") )
        clickElement(driver, el["btnLogin"])
        typeACharacter(driver, el["txtPassword"], os.getenv("PASSWORD"))
        clickElement(driver, el["btnLogin"])
        waitingAnElement(driver, el["txtWelcome"])
        clickElement(driver, el["linkCompany"])
        clickElement(driver, el["btnAddNewCompany"])
        typeACharacter(driver, el["txtCompanyName"], dataSet["companyName"] )
        typeACharacter(driver, el["txtInputEmail"], dataSet["companyEmail"] )
        typeACharacter(driver, el["txtInputPhone"], dataSet["companyPhone"] )
        clickElement(driver, el["dropDownIndsutryType"])
        clickElement(driver, el["optionIndustryType"])
        clickElement(driver, el["dropDownCompanyType"])
        clickElement(driver, el["optionCompanyType"])
        clickElement(driver, el["dropDownLanguage"])
        clickElement(driver, el["optionLanguage"])
        typeACharacter(driver, el["txtAddress"], dataSet["address"] )
        clickElement(driver, el["dropDownCountry"])
        clickElement(driver, el["optionCountry"])
        clickElement(driver, el["dropDownProvince"])
        scrollElement(driver, el["scrollView"], 300)
        clickElement(driver, el["optionProvince"])
        clickElement(driver, el["dropDownCity"])
        clickElement(driver, el["optionCity"])
        clickElement(driver, el["dropDownDistrict"])
        clickElement(driver, el["optionDistrict"])
        clickElement(driver, el["dropDownSubDistrict"])
        clickElement(driver, el["optionSubDistrict"])
        clickElement(driver, el["btnNext"])
        clickElement(driver, el["btnNext"])
        typeACharacter(driver, el["txtBranchName"], dataSet["branchName"] )
        clickElement(driver, el["btnFillSameData"])
        clickElement(driver, el["btnCheckTnC"])
        clickElement(driver, el["btnRegister"])
    finally:
        driver.quit()

def test_TC004_Validate_New_Company():
    driver = openDriver()
    try:
        el = getElementsWebsite(driver)
        wait = WebDriverWait(driver, 10)
        driver.get(os.getenv("BASEURL"))
        clickElement(driver, el["btnEmail"])
        typeACharacter(driver, el["txtEmail"], os.getenv("USERNAME") )
        clickElement(driver, el["btnLogin"])
        typeACharacter(driver, el["txtPassword"], os.getenv("PASSWORD"))
        clickElement(driver, el["btnLogin"])
        waitingAnElement(driver, el["txtWelcome"])
        clickElement(driver, el["linkCompany"])
        urutan = searchOnList(driver, el["listOfCompany"], dataSet["companyName"])
        clickElement(driver, f"(//button[contains(text(), 'Manage')])[{urutan}]")
        time.sleep(2)
        assert getText(driver, el["txtCompanyName"]) == dataSet["companyName"]
        assert getText(driver, el["txtInputEmail"]) == dataSet["companyEmail"]
        assert getText(driver, el["txtInputPhoneNumber"]) == dataSet["companyPhone"]
        assert getText(driver, el["txtCompanyAddress"]) == dataSet["address"]
        assert getValueOnOption(driver, dataSet["industryType"]) == dataSet["industryType"]
        assert getValueOnOption(driver, dataSet["companyType"]) == dataSet["companyType"]
        assert getValueOnOption(driver, dataSet["country"]) == dataSet["country"]
        assert getValueOnOption(driver, dataSet["province"]) == dataSet["province"]
        assert getValueOnOption(driver, dataSet["city"]) == dataSet["city"]
        assert getValueOnOption(driver, dataSet["district"]) == dataSet["district"]
    finally:
        driver.quit()
    



