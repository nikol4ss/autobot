from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

def input(driver, xpath: str, key: str, timeout=3):
    try:
        wait = WebDriverWait(driver, timeout)
        input = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input.clear()
        input.send_keys(key)
        return input

    except TimeoutException:
        print(f"[ERRO] Timeout: {xpath}")
    except Exception as e:
        print(f"[ERRO] {xpath}: {e}")
