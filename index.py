from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Kreiranje instance WebDriver-a (Chrome)
driver = webdriver.Chrome()

# Otvaranje Google pretrage
driver.get("https://www.google.com/")

# Pronalaženje elementa za unos teksta i slanje "facebook" kao pretrage
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("facebook")
search_box.send_keys(Keys.RETURN)

# Čekanje da se stranica učita
time.sleep(2)

# Pronalaženje linka ka Facebook-u i klik na njega
facebook_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Facebook")
facebook_link.click()

# Čekanje da se stranica učita
time.sleep(2)

# Pronalaženje elementa za unos email adrese i slanje pogrešnih informacija
email_box = driver.find_element(By.ID, "email")
email_box.send_keys("neispravanemail@neispravan.com")
password_box = driver.find_element(By.ID, "pass")
password_box.send_keys("pogresnalozinka")

# Pronalaženje dugmeta za login i klik na njega
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Čekanje da se stranica učita
time.sleep(2)

# Provera postojanja poruke o pogrešnim login informacijama
error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Pogrešna email adresa ili lozinka')]")
assert error_message.is_displayed()

# Zatvaranje browsera
driver.quit()
