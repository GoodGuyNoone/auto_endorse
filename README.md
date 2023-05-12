# auto_endorse

### HOW TO


1. Clone the repo
   ```sh
   git clone https://github.com/GoodGuyNoone/auto_endorse.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `.env.dist` in `.env` and fill in the required data.
4. Run script
    ```sh
    python endorse.py --link LINKTOPROFILE
    or
    python endorse.py -l LINKTOPROFILE
    
    example: python endorse.py -l https://www.linkedin.com/in/aleksandr-churakov/
    ```
    
<h3>How script is working:</h3>

1. Logging into LinkedIn account.
2. Opens up skills page of desired person.
3. Endorse all skills which is not endorsed before


I used to locate and click on element:

`self.browser.execute_script("arguments[0].scrollIntoView();", element)
self.browser.execute_script("arguments[0].click();", element)`

Another way to implement this functionality is to use the built-in Selenium ActionChains method move_to_element and click() on element.


----
<h3>Problems for now:</h3>

- ~~Script is able to endorse ~25 skills at once before page is reloaded using execute_script. One of the solutions is to remove the scroll to the required element and use only `execute_script("arguments[0].click();", element)`. Which allows us to click on an element if it`s not presented in page view.~~
- ~~If script is unable to click on every skill before page is reloaded, `stale element reference: element is not attached to the page document` error is raised~~

<h3>Concerns</h3>

- Any limitations of endorsements in a day?
- Can you get banned?

----

<h3>To do:</h3>

- ~~Add parsing of link user is provided as a parameter. python endorse --link=xxxx~~
- Two-factor authentication
- Resolve all problems
