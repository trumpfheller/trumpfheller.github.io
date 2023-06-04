---
layout: default
---

I want to automate my daily job search. 
Now this script 
1. uses the **webdriver.Chrome()** method to open a Chrome browser 
2. navigates to the Google Jobs search page. 
3. uses the **find_element_by_xpath()** method to locate the search input field 
4. enters the job title and location information. 
5. After waiting for 5 seconds for the search results to load, the script uses XPath selectors to locate the job listings on the page.
6. then uses the pandas library to export the search results to an Excel sheet named 'google_jobs.xlsx'. It creates a new DataFrame and iterates through each job listing, extracting the job title, company name, location, and link information. 
7. It appends this information to the DataFrame using the **df.append()** method and then exports the DataFrame to Excel using the **df.to_excel()** method.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Set up the Chrome driver
driver = webdriver.Chrome()

# Define job title and location to search for
job_title = "technical writing"
location = "California"

# Search on Google Jobs
driver.get('https://www.google.com/search?q=google+jobs')
search_input = driver.find_element_by_xpath('//input[@name="q"]')
search_input.send_keys(f'{job_title} {location}')
search_input.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5) 
google_jobs = driver.find_elements_by_xpath('//div[contains(@class, "card-content")]')

# Export search results to Excel
df = pd.DataFrame(columns=['Job Title', 'Company', 'Location', 'Link'])
for job in google_jobs:
    job_title = job.find_element_by_xpath('.//a').text
    company = job.find_element_by_xpath('.//span[1]').text
    location = job.find_element_by_xpath('.//span[2]').text
    link = job.find_element_by_xpath('.//a').get_attribute('href')
    df = df.append({'Job Title': job_title, 'Company': company, 'Location': location, 'Link': link}, ignore_index=True)
df.to_excel('google_jobs.xlsx', index=False)

# Take a screenshot of the page
driver.save_screenshot('google_jobs.png')

# Close the browser
driver.quit()
```

Next I want to get this done with Linkedin or Indeed(?) or - not sure yet.
