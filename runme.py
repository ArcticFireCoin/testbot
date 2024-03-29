from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set the WebDriver, use of Firefox() or Chrome() is also possible.
driver = webdriver.Chrome()
driver.get("https://coinhunt.cc")

# Get and click on all time best tab
all_time_best_tab = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/div/nav/a[1]")
all_time_best_tab.click()

# Need to wait here for the table to fully load
sleep(1)

# Get and click on show all button at bottom of table
show_more_button = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[12]")
show_more_button.click()

# Need to wait here for the rest of the table items to load
sleep(4)

# Find saveanimal img via the src tag. Then navigate to the grandparent which is the whole row. Then find vote button.
saveanimal_img = driver.find_element_by_xpath("//img[contains(@src,'https://i.ibb.co/g9P7Ct3/Logo-Project1-256.png')]")
g_parent = saveanimal_img.find_element_by_xpath("../..")
gg_parent = g_parent.find_element_by_xpath("./..")
button = gg_parent.find_element_by_class_name("btn")

# Click only of button has not been clicked yet. Useful in case the IP from apiscraper has already been used. Without this we might be undoing votes.
button_classes = button.get_attribute("class")

if "btn-success" in button_classes:
    print("Already clicked")
else:
    print("Clicking now...")
    button.click()
