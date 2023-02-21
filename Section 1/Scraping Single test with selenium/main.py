# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from selenium import webdriver

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
  driver.get("https://techbeamers.com/websites-to-practice-selenium-webdriver-online/#1httpsphptravelscomdemo")
  return driver

def main():
  driver = get_driver()
  #element = driver.findElements(By.xpath("///*[@id="post-1805"]/header/h1"));
  #element = driver.find_element(by="xpath", value="//*[@id="post-1805"]/header/h1")
  #element = driver. find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/article/header/h1")
  element = driver.find_element("xpath", '//*[@id="post-1805"]/header/h1')
  return element.text

print(main())