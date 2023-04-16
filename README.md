# auto_endorse

`python endorse.py -l https://www.linkedin.com/in/aleksandr-churakov/`

###How script is working:
1. Logging into LinkedIn account.
2. Opens up skills page of desired person.
3. Endorse all skills which is not endorsed before


I used to locate and click on element:

`self.browser.execute_script("arguments[0].scrollIntoView();", element)
self.browser.execute_script("arguments[0].click();", element)`

Another way to implement this functionality is to use the built-in Selenium ActionChains method move_to_element and click() on element.

----

###performance via scrollIntoView(): vs move_to_element()

| scrollIntoView()  | move_to_element() |
| ------------- | ------------- |
| Skills  | Skills  |
| Time  | Time  |
| Speed | Speed |

----
###Problems for now:
- Script is able to endorse ~25 skills at once before page is reloaded using execute_script. One of the solutions is to remove the scroll to the required element and use only `execute_script("arguments[0].click();", element)`. Which allows us to click on an element if it`s not presented in page view.
- If script is unable to click on every skill before page is reloaded, `stale element reference: element is not attached to the page document` error is raised

----

### To do:
- ~~Add parsing of link user is provided as a parameter. python endorse --link=xxxx~~
- Resolve all problems