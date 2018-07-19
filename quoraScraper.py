import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Con:
    link = ''
    upvotes = -1
    def __init__(self, link, upvotes):
        self.link = link
        self.upvotes = upvotes
    def __repr__(self):
        return '<li><a href="' +self.link +'">'+ str(self.link.split('/')[3]) + ' :: ' + str(self.upvotes) +'</a></li>'

browser=webdriver.Chrome('/Users/akshaymiterani/Python Development/chromedriver')
#browser=webdriver.PhantomJS()
browser.get('https://www.quora.com/')

username = "Email-ID"
password = "Password"
browser.find_elements_by_xpath("//input[@class='text header_login_text_box ignore_interaction']")[0].send_keys(username)
browser.find_elements_by_xpath("//input[@class='text header_login_text_box ignore_interaction']")[1].send_keys(password)
time.sleep(1)
browser.find_element_by_xpath("//input[@class='submit_button ignore_interaction']").click()
time.sleep(2)

browser.get('https://www.quora.com/stats/')
time.sleep(2)

menu = browser.find_element_by_class_name('menu_link')
menu.click()
options = browser.find_elements_by_class_name('menu_list_item')
options[3].click()
time.sleep(2)

storage = list()
event = browser.find_elements_by_class_name('pagedlist_item')
for items in event:
    items.click()
    time.sleep(2)
    stats = browser.find_elements_by_class_name('heads_up_item')
    link = items.find_element_by_css_selector('a').get_attribute('href')
    upvotes = stats[1].text.split('\n')[0]
    if(upvotes.endswith("k")):
        upvotes = int(float(upvotes[0:len(upvotes)-1])*1000)
    con = Con(link, int(upvotes))
    print con
    storage.append(con)
    time.sleep(2)

storage.sort(key=lambda x: x.upvotes, reverse=True)
print storage

for s in storage:
    print s
