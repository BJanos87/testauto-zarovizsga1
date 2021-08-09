# Szükséges komponensek beimportálása
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Driver felparaméterezése
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Használni kívánt oldal megnyitása
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")

    # Web element-ek letárolása változókba
    input_field_a = driver.find_element_by_id("a")
    input_field_b = driver.find_element_by_id("b")
    submit_btn = driver.find_element_by_id("submit")
    result_field = driver.find_element_by_id("result")

    # TC01
    input_field_a.send_keys(99)
    input_field_b.send_keys(12)
    submit_btn.click()
    time.sleep(0.5)
    assert result_field.text == str(222)
    input_field_a.clear()
    input_field_b.clear()

    #TC 02
    input_field_a.send_keys("kiskutya")
    input_field_b.send_keys(12)
    submit_btn.click()
    time.sleep(0.5)
    assert result_field.text == "NaN"
    input_field_a.clear()
    input_field_b.clear()

    #TC 03
    input_field_a.send_keys("")
    input_field_b.send_keys("")
    submit_btn.click()
    time.sleep(0.5)
    assert result_field.text == "NaN"
    input_field_a.clear()
    input_field_b.clear()

except AssertionError as err:
    print("A megjelenítésre került érték, nem egyezik meg az elvárt értékkel", err)

finally:
    driver.close()
    driver.quit()






