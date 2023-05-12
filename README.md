## DISCLAIMER: this is only for study purposes. Use it at your own risk!
![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
)

### WHAT`S THAT

An automated script for LinkedIn skill endorsements. Say goodbye to the tedium of manually endorsing skills and let this script handle the task for you, saving time and effort.
This script allows you to automate the process of endorsing skills of your desired LinkedIn profile or multiple ones.

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
4. Create `profiles.txt` file and fill it with links to profiles if you want to endorse in bulk.
5. Run script
    ```sh
    python endorse.py --link LINKTOPROFILE
    ```
   or
   ```sh
   python endorse.py --file
   ```
   ```sh
   example: python endorse.py --link https://www.linkedin.com/in/aleksandr-churakov/
   python endorse.py --file
   ```
        
<h3>How script is working:</h3>

1. Logging into LinkedIn account.
2. Opens up skills page of person.
3. Endorsing all skills which is not endorsed before


----

<h3>Problems for now:</h3>

- ~~Script is able to endorse ~25 skills at once before page is reloaded using execute_script. One of the solutions is to remove the scroll to the required element and use only `execute_script("arguments[0].click();", element)`. Which allows us to click on an element if it`s not presented in page view.~~
- ~~If script is unable to click on every skill before page is reloaded, `stale element reference: element is not attached to the page document` error is raised~~

----
<h3>Concerns</h3>

- Any limitations of endorsements in a day?
- Can you get banned?

----

<h3>To do:</h3>

- ~~Add parsing of link user is provided as a parameter. python endorse --link=xxxx~~
- Two-factor authentication
- Resolve all problems
