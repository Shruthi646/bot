from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select

path = "/Users/shruthireddy/Desktop/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://app.fundingxchange.co.uk/captureRequirements.do?affiliate=msm&cohort=msm_medium")
print(driver.title)

amount = driver.find_element_by_id("loanAmount")
amount.send_keys("5,000")
amount.send_keys(Keys.RETURN)

purpose = driver.find_element_by_id("loanPurpose")
purpose_options = Select(purpose)
#purpose_options.select_by_index(random.randint(0, len(purpose_options.options) - 1))
purpose_options.select_by_index(random.randint(1, len(purpose_options.options)))
#purpose_options.select_by_visible_text("Cash flow/working capital")
#print(len(purpose_options.options))
#all_options= purpose_options.options
#for opts in all_options:
    #print(opts.text)

#APR = driver.find_elements_by_class_name("vertical-align-middle")
#print(APR)



#drpdown_purpose = driver.find_element_by_xpath("//*[@id='loanPurpose']/options")
#print(drpdown_purpose)


submit = driver.find_element_by_id("getFundedPublic")
submit.send_keys(Keys.RETURN)



#driver.quit()