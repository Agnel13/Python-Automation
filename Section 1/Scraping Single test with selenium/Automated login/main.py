# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from selenium import webdriver
import time

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver


def main():
  driver = get_driver()
  driver.find_element("id", 'id_username').send_keys("automated")
  time.sleep(2)
  driver.find_element("id", 'id_password').send_keys("automatedautomated")  
  time.sleep(2)
  driver.find_element("xpath", '/html/body/div[1]/div/div/div[3]/form/button').click 
  time.sleep(2)
  #element = driver.findElements(By.xpath("///*[@id="post-1805"]/header/h1"));
  #element = driver.find_element(by="xpath", value="//*[@id="post-1805"]/header/h1")
  #element = driver. find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/article/header/h1")
  #element = driver.find_element("xpath", '//*[@id="displaytimer"]')
  print(driver.current_url)


print(main())