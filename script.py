from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail():
    # Set your email and password
    email = "tejas27dhanani@gmail.com"
    password = "ipuojlnujjpuqzbj"

    # Set up the server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create an SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email, password)

    # Compose the email
    from_email = email
    to_email = "tejas27dhanani@gmail.com"
    subject = "Volleyball Slot Available"
    message = "Volleyball slot is available"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())

    # Quit the server
    server.quit()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = "https://anc.ca.apm.activecommunities.com/burnaby/activity/search/detail/15640?onlineSiteId=0&from_original_cui=true"

while True:
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)

    enrollment_section = driver.find_element(
        By.CLASS_NAME, 'activity-enrollment__section')

    activity_status = enrollment_section.find_element(
        By.CLASS_NAME, 'activity-status').get_attribute('innerHTML')

    if activity_status != 'Full':
        sendEmail()
        enrollment_section.find_element(
            By.CLASS_NAME, 'btn').click()

        inputs = driver.find_elements(By.CLASS_NAME, 'input')

        inputs[0].send_keys("ranipayash01@gmail.com")
        inputs[1].send_keys("lynnLake@23")

        driver.find_element(
            By.CLASS_NAME, 'btn').click()

        time.sleep(1)

        dropdown_button = driver.find_element(
            By.XPATH, "//div[@class='dropdown__button input__field']")

        dropdown_button.click()

        participant = driver.find_element(
            By.XPATH, """/html/body/div[1]/div/div/div/div[4]/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/ul/li""")
        participant.click()

        addToCart_button = driver.find_element(
            By.XPATH, """//*[@id="main-content-body"]/div/div[3]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/button"""
        )
        addToCart_button.click()
        time.sleep(1)

        finish_button = driver.find_element(By.CSS_SELECTOR ,'button[data-qa-id="shopping-cart-orderSummary-checkoutBtn"]')
        finish_button.click()

        break;

    else:
        time.sleep(4)
        driver.quit()
