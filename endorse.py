import argparse

from environs import Env
from selenium import webdriver
from selenium.webdriver.common.by import By

from actions import Actions

# parser of profile link from command line
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--link", required=True,
                help="link to LinkedIn profile ex:https://www.linkedin.com/in/aleksandr-churakov/")
args = vars(ap.parse_args())

main_page = "https://linkedin.com"
browser = webdriver.Chrome()
env = Env()
env.read_env(".env")

try:
    browser.get(main_page)
    login_input = browser.find_element(By.CSS_SELECTOR, "#session_key")
    login_input.clear()
    login_input.send_keys(env.str("LINKEDIN_LOGIN"))
    password_input = browser.find_element(By.CSS_SELECTOR, "#session_password")
    password_input.clear()
    password_input.send_keys(env.str("LINKEDIN_PASSWORD"))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.get(f"{args['link'].rstrip('/')}/details/skills/")
    actions = Actions(browser)
    actions.scroll_down()
    actions.endorse_skills()
except Exception as ex:
    print(ex)
finally:
    browser.quit()
