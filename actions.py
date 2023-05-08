import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SCROLL_PAUSE_TIME = 1


class Actions():
    def __init__(self, browser):
        self.browser = browser

    def scroll_down(self):
        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                time.sleep(2)
                break
            last_height = new_height

    def endorse_skills(self, link=None):
        try:
            endorse_skills = self.browser.find_elements(By.XPATH, "//Span[text()='Endorse']")

            while int(len(endorse_skills)) != 0:
                for element in endorse_skills:
                    if element.is_displayed():
                        # click on every button presented
                        self.browser.execute_script("arguments[0].click();", element)

                time.sleep(3)
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[text()='All']")))
                self.scroll_down()
                endorse_skills = self.browser.find_elements(By.XPATH, "//Span[text()='Endorse']")
                print(f"inside while loop - {len(endorse_skills)}")

            endorsed_skills = self.browser.find_elements(By.XPATH, "//Span[text()='Endorsed']")
            num_endorsed_skills = 0
            for skill in endorsed_skills:
                if skill.is_displayed():
                    num_endorsed_skills += 1

        finally:
            print(f"{link.rstrip('/')} - {int(num_endorsed_skills)} skills are endorsed")
