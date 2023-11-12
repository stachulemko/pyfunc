from telnetlib import STATUS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service


def register_and_check_email_availability(emails):

    driver = webdriver.Chrome()

    """EdgeService = Service(
        r"C:\\tools\\msedgedriver.exe")
    driver = webdriver.Edge(service=EdgeService)"""

    driver.get("https://1login.wp.pl/rejestracja?client_id=poczta_nh&flow=registration&login_challenge=Cj0KJDExZDAzYzQ3NzRmYWU4YWM3NTE5OTMxZTEzMjY3YjgwMTk4YhDXsIqqBhoPCglwb2N6dGFfbmgSAnYxEiBM2knrm1m7rs3uva7bLZJT43P7h7pyHsezToSzt2-4kw&registrationFlow=newForced&registrationBrand=wp")

    # Wprowadź dane rejestracji (zakładam, że to jest przykład)
    driver.find_element(By.NAME, 'name').send_keys("Imie")
    driver.find_element(By.NAME, "lastName").send_keys("Nazwisko")
    driver.find_element(By.NAME, "sex").send_keys("M")
    driver.find_element(By.ID, "date").send_keys("6")
    select_month = driver.find_element(By.ID, "month")
    select = Select(select_month)
    select.select_by_value('2')

    driver.find_element(By.ID, "year").send_keys("1940")

    # Wprowadź e-mail w polu rejestracji

    driver.find_element(By.ID, "login").send_keys(emails[0])

    # Kliknij przycisk "Zarejestruj się"
    time.sleep(8)
    # element = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, '//button[text()="Dalej"]'))
    # )
    # while not driver.find_element(By.XPATH, '//button[text()="Dalej"]').():
    # print("czkamsd")
    # time.sleep(1)
    """ while True:
        is_clicable = False
        try:
            driver.find_element(By.XPATH, '//button[text()="Dalej"]').click()
            is_clicable = True
        except WebDriverException:
            print("Element is not clickable")
        if is_clicable:
            break """

    # driver.find_element(
    #    By.CSS_SELECTOR, "sc-bcXHqe Buttons__Button-sc-g2fyk2-0 iGblCX gwugjh").click()

    # Sprawdź, czy pojawi się informacja o błędzie rejestracji lub o dostępności adresu e-mail
    # error_message = driver.find_element(
    # By.XPATH, '//div[text()="Podany login jest już zajęty"')
    # driver.find_element(By.XPATH, "//*[text()='Podany login jest już zajęty']")
    # driver.find_element(
    #    By.CLASS_NAME, "sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV")
    time.sleep(8)
    x = driver.find_element(
        By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
    print(x.tag_name)
    print(x.text)

    for email in emails[1:]:
        print(f"wstawiamy: {email}")
        driver.find_element(By.ID, "login").send_keys("")
        driver.find_element(By.ID, "login").clear()
        driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
        #driver.refresh(By.ID, "login")
        # WebDriverWait(driver, 10).until(
        #    EC.text_to_be_present_in_element_value((By.ID, "login"), ""))
        #print("czekamy na wyczyszczenie loginu ")
        # WebDriverWait(driver, 10).until(
        #    EC.staleness_of(driver.find_element(By.ID, "login")))
        print(f'login:{driver.find_element(By.ID, "login").text}')

        time.sleep(random.randint(1, 3))
        driver.find_element(By.ID, "login").send_keys(email)
        #print(f'login:{driver.find_element(By.ID, "login").text}')
        time.sleep(1)
        x = driver.find_element(
            By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
        # print(x)
        print(x.text)

    # if "nie istnieje" in error_message.text:
    #    return False  # Adres e-mail nie istnieje
    # else:
    #    return True  # Adres e-mail istnieje


email_to_check = ["anna", "kowal", "dadasdfgfasfafda", "akepka"]
register_and_check_email_availability(email_to_check)
