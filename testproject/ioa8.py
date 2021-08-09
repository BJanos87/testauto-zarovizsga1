# Szükséges komponensek beimportálása
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Driver felparaméterezése
driver = webdriver.Chrome(ChromeDriverManager().install())

# Használni kívánt oldal megnyitása
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")

# A Python-al kiszámolt eredmény tárolására szolgáló változó,
# None típus, mert később lehet (int, float)
result = None

# Számításhoz használt függvények deklarálása


def python_add(a, b):
    global result
    result = a + b
    return result


def python_subtraction(a, b):
    global result
    result = a - b
    return result


def python_multiplication(a, b):
    global result
    result = a * b
    return result


def python_division(a, b):
    global result
    result = a / b
    return result


try:
    # Web element-ek letárolása változókba
    num1_value_web = driver.find_element_by_id("num1")
    num2_value_web = driver.find_element_by_id("num2")
    operator = driver.find_element_by_id("op")
    calculate_btn = driver.find_element_by_id("submit")
    result_web = driver.find_element_by_id("result")

    # Python számításhoz használni kívánt változók létrehozása
    python_num1 = int(num1_value_web.text)
    python_num2 = int(num2_value_web.text)
    python_op = operator.text

    # Calculate gomb használata
    calculate_btn.click()
    time.sleep(2)

    # Az oldalon kapott matamatikai művelettől függően szükséges függvény meghívása
    if python_op == "+":
        python_add(python_num1, python_num2)

    elif python_op == "-":
        python_subtraction(python_num1, python_num2)

    elif python_op == "*":
        python_multiplication(python_num1, python_num2)

    elif python_op == "/":
        python_division(python_num1, python_num2)

    # Python által kiszámított eredmény kiiratása
    print(result)

    # Oldalon megjelenítésre került eredmény összehasonlítás a Python-nal számított eredménnyel
    assert str(result) == result_web.text

    # AssertionError kezelés
except AssertionError as err:
    print("Az oldalon megjelenített eredmény nem megfelelő", err)

    # Megnyitott weblap bezárásra kerül
finally:
    driver.close()
    driver.quit()
