import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import *

DRIVER_PATH ='' #chrome driver path
ACCOUNT = {'username':'','passwd': ''} #Enter username and password
IG_POST ='https://www.instagram.com/p/' #Enter ur of desired post to inspect


#Selenium Setup
options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome( executable_path=driverpth,options=options)

#Login
driver.get("https://www.instagram.com/accounts/login/?hl=es")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(accounts['username'])
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(accounts['passwd'])
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
time.sleep(3)

#Go to post
driver.get(IG_POST)
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/section/div/div[2]/div[4]/button').click()
except:
    print('nothing')
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class, 'zV_Nj')]").click()
time.sleep(2)


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
#Get list of accounts that liked the post
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(2)
elems = driver.find_elements_by_css_selector('.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm:not([aria-labelledby])')
time.sleep(2)
users = []

#Once we get the list we start to navigate through each of one and we go to their profile and like their first post
for elem in elems:
    users.append(elem.text)
    print('Title : ' +elem.text)
print('done')
print('Total users in list:'+users.__len__().__str__())

print('process of liking')
count =0
for user in users:
    if count==300:
        break
    count+=1
    print(count)
    time.sleep(2)
    driver.get('https://www.instagram.com/'+user)
    time.sleep(2)
    posts = driver.find_elements_by_css_selector('._9AhH0')
    time.sleep(1)
    if len(posts)>0:
        post=posts[0]
        driver.execute_script("arguments[0].scrollIntoView();", post)
        post.click()
        time.sleep(2)
        try:
            likebtn= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[1]/button')
            driver.execute_script("arguments[0].scrollIntoView();", likebtn)
            likebtn.click()
            time.sleep(1)
        except NoSuchElementException:
            ""
        time.sleep(1)



