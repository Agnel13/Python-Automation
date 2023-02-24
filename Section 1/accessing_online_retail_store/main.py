from selenium import webdriver
import time

def get_driver():
  option = webdriver.ChromeOptions()
  option.add_argument("disable-infobars")
  option.add_argument("start-maximized")
  option.add_argument("disable-dev-shm-usage")
  option.add_argument("no-sandbox")
  option.add_experimental_option("excludeSwitches", ["enable-automation"])
  option.add_argument("disable-blink-features=AutomationControlled")  
  
  driver = webdriver.Chrome(options=option)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

def clean_text(element):
  output = element.split(" ")[0]
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  driver.find_element("id", 'CustomerEmail' ).send_keys("Agnel@gmail.com")
  time.sleep(2)
  driver.find_element("id", 'CustomerPassword' ).send_keys("Agnel@13")
  time.sleep(2)
  driver.find_element("xpath",'//*[@id="customer_login"]/button').click()
  time.sleep(2)
  driver.find_element("xpath",'/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
  time.sleep(2)
  #element = driver.find_element("xpath",'/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a')
  #element = driver.find_element("xpath",'//*[@id="shopify-section-page-contact-us"]/section/div/h1')
  element = driver.find_element("xpath", '//*[@id="shopify-section-page-contact-us"]/section/div/h1')
  return clean_text(element.text)

print(main())
