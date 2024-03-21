from selenium import webdriver

from app.page_objects.dice.dice_login_page import DiceLoginPage

driver = webdriver.Chrome()

driver.get('https://www.dice.com/dashboard/login')

loginPage = DiceLoginPage(driver)

loginPage.enter_email("andrewkassab@live.com")\
    .enter_password("glds1$sFm%")
loginPage.click_login_button()





