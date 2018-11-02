from selenium import webdriver
from getpass import getpass
#print(dir(selenium))
#print(dir(getpass))

usr = input("enter your username or email:")
pwd = input("enter your password:")
#pwd = getpass("enter your password:")

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

username_box = driver.find_element_by_id("email")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(pwd)

login_btn = driver.find_elemint_by_id("u_0_2")
login_btn.submit()
