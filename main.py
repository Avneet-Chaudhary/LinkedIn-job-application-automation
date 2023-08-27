from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

LINKEDIN_EMAIL = "your email"
LINKEDIN_PASSWORD = "pass....."
mob_no = "123*******"


chrome_driver_path = "path...."
driver = webdriver.Chrome(chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(2)

Sign_in = driver.find_element(by=By.LINK_TEXT, value='Sign in')
Sign_in.click()
time.sleep(4)
# driver.quit()

username = driver.find_element_by_id("username")
username.send_keys(LINKEDIN_EMAIL)

passwrd = driver.find_element_by_id("password")
passwrd.send_keys(LINKEDIN_PASSWORD)

signin_btn = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button")
signin_btn.click()
time.sleep(2)


all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(mob_no)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
