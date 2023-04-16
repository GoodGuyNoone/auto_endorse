import time

from selenium.webdriver.common.by import By

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
                break
            last_height = new_height

    def endorse_skills(self):
        try:
            endorse_skills = self.browser.find_elements(By.XPATH, "//Span[text()='Endorse']")
            skills_to_endorse = int(len(endorse_skills) / 2)
            print(str(skills_to_endorse) + " skills to be endorsed")
            endorsed_skills = 0
            for element in endorse_skills:
                # scrolling to element that is will be visible on screen
                # self.browser.execute_script("arguments[0].scrollIntoView();", element)
                # click on the element
                self.browser.execute_script("arguments[0].click();", element)
                endorsed_skills += 0.5
        finally:
            print(f"{int(endorsed_skills)}/{skills_to_endorse} skills is endorsed")
