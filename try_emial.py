from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


def register_and_check_email_availability(email):
    # Możesz użyć dowolnej przeglądarki, dla której masz odpowiednie sterowniki
    driver = webdriver.Chrome()
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
    driver.find_element(By.ID, "login").send_keys(email)

    # Kliknij przycisk "Zarejestruj się"
    time.sleep(8)
    driver.find_element(By.XPATH, '//button[text()="Dalej"]').click()
    # driver.find_element(
    #    By.CSS_SELECTOR, "sc-bcXHqe Buttons__Button-sc-g2fyk2-0 iGblCX gwugjh").click()

    # Sprawdź, czy pojawi się informacja o błędzie rejestracji lub o dostępności adresu e-mail
    # error_message = driver.find_element(
    # By.XPATH, '//div[text()="Podany login jest już zajęty"')
    # driver.find_element(By.XPATH, "//*[text()='Podany login jest już zajęty']")
    # driver.find_element(
    #    By.CLASS_NAME, "sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV")
    time.sleep(3)
    x = driver.find_element(
        By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")

    # if "nie istnieje" in error_message.text:
    #    return False  # Adres e-mail nie istnieje
    # else:
    #    return True  # Adres e-mail istnieje

    print(x.tag_name)
    print(x.text)
    print("xx")
    driver.find_element(By.ID, "login").send_keys("kowal")
    time.sleep(3)
    x = driver.find_element(
        By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
    print(x.text)
    




email_to_check = "anna"
if register_and_check_email_availability(email_to_check):
    print(f"Adres e-mail '{email_to_check}' istnieje.")
else:
    print(f"Adres e-mail '{email_to_check}' nie istnieje.")
