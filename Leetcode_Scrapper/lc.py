# Import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the chromedriver service
s = Service('chromedriver.exe')

# Instantiate the webdriver
driver = webdriver.Chrome(service=s)

# The base URL for the pages to scrape
page_URL = "https://leetcode.com/problemset/all/?page="

# Function to get all the 'a' tags from a given URL


def get_a_tags():
    # Load the URL in the browser
    driver.current_url
    # Wait for 7 seconds to ensure the page is fully loaded
    time.sleep(7)
    # Find all the 'a' elements on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    ans = []
    # Iterate over each 'a' element
    for i in links:
        try:
            # Check if '/problems/' is in the href of the 'a' element
            if "/problems/" in i.get_attribute("href"):
                # If it is, append it to the list of links
                ans.append(i.get_attribute("href"))
        except:
            pass
    # Remove duplicate links using set
    ans = list(set(ans))
    return ans

def get_all_links(url,total_pages):

    #load the url in chrome
    driver.get(url)
    #wait for the page to load
    time.sleep(7)

    links=[]

    for i in range(1,total_pages+1):
        links+=get_a_tags()
        if i!=total_pages:
            X_PATH = "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[3]/nav/button[10]"
            element=driver.find_element("xpath",X_PATH)
            element.click()
            time.sleep(7)
    links=list(set(links))
    return links

total_pages=55
links=[]
links = get_all_links(page_URL+str(1),total_pages)
links=list(set(links))



# Open a file to write the results to
with open('lc.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in links:
        # Write each link to the file, followed by a newline
        f.write(j+'\n')

# Print the total number of unique links found
print(len(links))

# Close the browser
driver.quit()