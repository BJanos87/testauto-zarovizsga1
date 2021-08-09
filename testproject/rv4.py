# Szükséges komponensek beimportálása
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Driver felparaméterezése
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Használni kívánt oldal megnyitása
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")

    # Web element-ek letárolása változókba
    text_field = driver.find_element_by_id("cites")
    cities_list = driver.find_elements_by_tag_name("li")
    missing_city_field = driver.find_element_by_id("missingCity")
    submit_btn = driver.find_element_by_id("submit")

    # Text mezőben található szöveg átalakítása listáva
    text_field_list = text_field.text.replace('"', '').replace(', ', ',').split(',')

    # Az oldal alsó részében található felsorolt nevek egy listába konvertálása
    city_list = []
    for city in cities_list:
        city_list.append(city.text)

    # Végigiterálás az elemeken és a két lista összehasonlítása,
    # majd a különbség bevitele a mezőbe
    for city in text_field_list:
        if city in city_list:
            continue
        else:
            missing_city = city
            print(missing_city)
            missing_city_field.send_keys(missing_city)

    # Submit gomb megnyomás
    submit_btn.click()
    time.sleep(1)

    result_field = driver.find_element_by_id("result")

    assert result_field.text == "Eltaláltad."

    # AssertionError kezelés
except AssertionError as err:
    print("Az oldalon megjelenített eredmény nem megfelelő", err)

    # Megnyitott weblap bezárásra kerül
finally:
    driver.close()
    driver.quit()
