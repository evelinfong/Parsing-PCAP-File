import time
import datetime
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Run the script in python3 instead of python
Make sure you install the Chrome webdriver and place it in your System path:
https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

#prompt user for email
emailA = input('What is your email address? ')
type(emailA)

#prompt user for password
passWord = getpass.getpass();

emailR = input('What is the recipient Email Address ');
type(emailR);

msgSubject = input('Enter the Subject: ');
type(msgSubject);

driver= webdriver.Chrome();
driver.get('https://mail.google.com/mail/u/0/');
driver.find_element_by_id('identifierId').send_keys(emailA);
driver.find_element_by_id('identifierNext').click();
time.sleep(1);
driver.find_element_by_name('password').send_keys(passWord);
driver.find_element_by_id('passwordNext').click();
time.sleep(5);
driver.find_element_by_xpath(".//*[text()= 'Compose']").click();
time.sleep(4);
driver.find_element_by_name('to').send_keys(emailR);
driver.find_element_by_name('subjectbox').send_keys(msgSubject);
time.sleep(2)


'''
TODO:
msgContent = input("Enter the content of the message: ");
type(msgContent);

msgContent = "\n".join(msgContent.split("\n"))
driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys(msgContent);
'''