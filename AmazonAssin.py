from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()                                           # Driver is open in chrome
driver.get("https://www.amazon.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(5)
print(driver.title)

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Wrist Watch")
time.sleep(3)
Option_List = driver.find_elements(By.XPATH, "//div[text()='wrist watch']")
print(len(Option_List))
time.sleep(3)

for ele in Option_List:
    print(ele.text)
    if ele.text == "wrist watch":
        ele.click()
        break

Option_List1 = driver.find_elements(By.XPATH, "//span[@data-csa-c-content-id='p_89/Titan']")
print(len(Option_List1))
time.sleep()


for ele in Option_List1:
    print(ele.text)
    if ele.text == "Titan":
        ele.click()
        break

driver.find_element(By.XPATH, "//span[text()='Analogue']").click()
time.sleep(3)

Cart_Element = driver.find_element(By.XPATH, "//div[@id='nav-cart-text-container']")
Cart_Element.click()
time.sleep(3)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(6)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(6)

driver.find_element(By.XPATH,"//span[text()='Leather']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//span[text()='25% Off or more']").click()
time.sleep(3)

time.sleep(3)
driver.quit()











