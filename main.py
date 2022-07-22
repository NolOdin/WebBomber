from selenium import webdriver


driver = webdriver.Chrome("F:\PyPro\WhatsAppBomber\chromedriver.exe")

driver.get("https://web.whatsapp.com/")

print("login")

name = input('Enter name: ')
count = int(input('enter count: '))
msg = input('Enter message: ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')

for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    sendButton.click()