from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)


# Locate the username and password fields and enter their specific values
username_field = driver.find_element(By.NAME, "username").send_keys("Admin")
password_field = driver.find_element(By.NAME, "password").send_keys("admin123")



# Locate the login button
login_button = driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")

time.sleep(5)

