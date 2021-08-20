from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

path = "/Users/shruthireddy/Desktop/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://app.fundingxchange.co.uk/captureRequirements.do?affiliate=msm&cohort=msm_medium")
print(driver.title)

amount = driver.find_element_by_id("loanAmount")
amount.send_keys("5,000")
#amount.send_keys(Keys.RETURN)

purpose = driver.find_element_by_id("loanPurpose")
purpose_options = Select(purpose)
purpose_options.select_by_index(random.randint(1, len(purpose_options.options)))
selectedPurpose = purpose_options.first_selected_option.text
print(selectedPurpose)


#PO = purpose_options


trading = driver.find_element_by_id("revenueMonths")
trading_options = Select(trading)
trading_options.select_by_visible_text("12 to 17 months")

#purpose_options.select_by_visible_text("Cash flow/working capital")

submit = driver.find_element_by_id("getFundedPublic")
submit.send_keys(Keys.RETURN)


with open("trial.csv", "w+") as file:
    bot_inputs = csv.writer(file)
    bot_inputs.writerow(["Amount", "Purpose", "Company Type", "Trading period"])
    bot_inputs.writerow([amount, selectedPurpose])

    
#purpose_options.select_by_index(random.randint(0, len(purpose_options.options) - 1))
#purpose_options.select_by_visible_text("Cash flow/working capital")    this line only selects one option from the drop down list
#print(len(purpose_options.options))                                    prints number of dropdown options
#all_options= purpose_options.options
#for opts in all_options:
    #print(opts.text)                                                   prints dropdown options in text format                                                 

#APR = driver.find_elements_by_class_name("vertical-align-middle")      unrelated, for the last page of MSM
#print(APR)



#drpdown_purpose = driver.find_element_by_xpath("//*[@id='loanPurpose']/options")
#print(drpdown_purpose)


submit = driver.find_element_by_id("getFundedPublic")
submit.send_keys(Keys.RETURN)



#driver.quit()
