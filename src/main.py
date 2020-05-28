from constant import constants
from selenium import webdriver
import time

def order(o):

	driver = webdriver.Chrome('PATH') # Change PATH to your chromedriver PATH
	driver.get(o['product_url'])

	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click() # Don't touch this parameter
	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(o["name"])
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(o["email"])
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(o["phone_number"])
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(o["address"])
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(o["zip"])
	driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(o["city"])
	driver.find_element_by_xpath('//*[@id="cnb"]').send_keys(o["card_number"])
	driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[0]').click() # Month Option
	driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[0]').click() # Month Year
	driver.find_element_by_xpath('//*[@id="vval"]').send_keys(o["cvv"])
# State
	driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[13]').click() # Don't touch this parameter
# Terms and Conditions
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click() # Don't touch this parameter
# Payment
	driver.find_element_by_xpath('//*[@id="button checkout"]/input').click()

if __name__ == '__main__':
	order(constants)