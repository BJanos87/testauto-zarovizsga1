# Szükséges komponensek beimportálása
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Driver felparaméterezése
driver = webdriver.Chrome(ChromeDriverManager().install())

# Használni kívánt oldal megnyitása
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")

try:
    # Használni kívánt gomb letárolása egy változóba
    submit_btn = driver.find_element_by_tag_name("button")

    # Submit gomb megnyomása 100-szor
    for _ in range(100):
        submit_btn.click()
    time.sleep(0.5)

    # Oldalon megjelenítésre került eredmény kigyűjtése egy listába
    results_list = driver.find_elements_by_tag_name("li")

    # A számláló deklarálása
    head_counter = 0

    # A már kigyűjtött eredmény lista végigiterálása, és kiértékelése
    for result in results_list:
        if result.text == "fej":
            head_counter += 1
        else:
            continue
    print(f'"fej" esetek száma:{head_counter}')

    # Eredmény ellenőrzése, hogy legalább 30 esetben jött ki a "fej"
    assert head_counter >= 30

    # AssertionError kezelés
except AssertionError as err:
    print("A fej 30-nál kevesebb esetben került kiiratásra", err)

    # Megnyitott weblap bezárásra kerül
finally:
    driver.close()
    driver.quit()
