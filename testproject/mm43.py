# Szükséges komponensek beimportálása
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Driver felparaméterezése
driver = webdriver.Chrome(ChromeDriverManager().install())

# Használni kívánt oldal megnyitása
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")

try:
    # Web element-ek letárolása változókba
    email_field = driver.find_element_by_id("email")
    submit_btn = driver.find_element_by_id("submit")

    # Teszt adatok
    test_data = "teszt@elek.hu"
    wrong_test_data = "teszt@"
    wrong_test_data_msg = "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."
    empty_test_data_msg = "Kérjük, töltse ki ezt a mezőt."

    # TC01
    email_field.send_keys(test_data)
    submit_btn.click()
    time.sleep(1)
    empty_msg_field = driver.find_elements_by_xpath("/html/body/div/div/form/div")
    assert len(empty_msg_field) == 0
    email_field.clear()

    # TC02
    email_field.send_keys(wrong_test_data)
    submit_btn.click()
    time.sleep(1)
    error_web_element = driver.find_element_by_xpath("/html/body/div/div/form/div")
    assert error_web_element.text == wrong_test_data_msg
    email_field.clear()

    # TC03
    email_field.send_keys("")
    submit_btn.click()
    time.sleep(1)
    error_web_element = driver.find_element_by_xpath("/html/body/div/div/form/div")
    assert error_web_element.text == empty_test_data_msg
    email_field.clear()

    # AssertionError kezelés
except AssertionError as err:
    print("Az oldalon megjelenített eredmény nem megfelelő", err)

    # Megnyitott weblap bezárásra kerül
finally:
    driver.close()
    driver.quit()
