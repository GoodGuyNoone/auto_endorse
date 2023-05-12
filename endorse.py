import argparse

from environs import Env
from selenium import webdriver
from selenium.webdriver.common.by import By

from actions import Actions


def endorse(link=None, file=False):
    browser = webdriver.Chrome()

    try:
        env = Env()
        env.read_env(".env")

        main_page = "https://linkedin.com"
        browser.get(main_page)
        login_input = browser.find_element(By.CSS_SELECTOR, "#session_key")
        login_input.clear()
        login_input.send_keys(env.str("LINKEDIN_LOGIN"))
        password_input = browser.find_element(By.CSS_SELECTOR, "#session_password")
        password_input.clear()
        password_input.send_keys(env.str("LINKEDIN_PASSWORD"))
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        if file:
            with open('profiles.txt') as profiles:
                for profile in profiles:
                    browser.get(f"{profile}/details/skills/")
                    actions = Actions(browser)
                    actions.scroll_down()
                    actions.endorse_skills(profile)
                profiles.close()
        else:
            browser.get(f"{link}/details/skills/")
            actions = Actions(browser)
            actions.scroll_down()
            actions.endorse_skills(link)

    except Exception as ex:
        print(ex)

    finally:
        browser.quit()


def main():
    # parser of arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--link", help="Link to LinkedIn profile ex:https://www.linkedin.com/in/aleksandr"
                                             "-churakov/", required=False, type=str, default=None)
    parser.add_argument("-f", "--file", help="Use it if you want to endorse skills for profiles from file",
                        action='store_const', const=True, required=False, default=False)
    args = parser.parse_args()

    # print(args)
    # print(type(args.file))

    # decide if we want use link from command line or list of profiles from file.
    if args.link:
        endorse(link=args.link)
    elif args.file:
        endorse(file=args.file)
    else:
        print("Specify parameter you are using or --help")


if __name__ == "__main__":
    main()
