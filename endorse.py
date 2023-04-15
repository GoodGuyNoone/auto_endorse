import time

from environs import Env
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://www.linkedin.com/in/aleksandr-churakov/"
browser = webdriver.Chrome()
env = Env()
env.read_env(".env")

try:
    browser.get("https://linkedin.com")
    login_input = browser.find_element(By.CSS_SELECTOR, "#session_key")
    login_input.clear()
    login_input.send_keys(env.str("LINKEDIN_LOGIN"))
    password_input = browser.find_element(By.CSS_SELECTOR, "#session_password")
    password_input.clear()
    password_input.send_keys(env.str("LINKEDIN_PASSWORD"))
    # browser.get(f"{link.rstrip('/')}/details/skills/")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    browser.quit()

