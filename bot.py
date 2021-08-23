from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import random

path = "/Users/shruthireddy/Desktop/chromedriver"
driver = webdriver.Chrome(path)




driver.get("https://app.fundingxchange.co.uk/captureRequirements.do?affiliate=msm&cohort=msm_medium")
print(driver.title)                                                 #tester code: Unrequired


amount_generator = random.randint(10000, 150000)             
amount = driver.find_element_by_id("loanAmount").send_keys(amount_generator)


purpose = driver.find_element_by_id("loanPurpose")
purpose_options = Select(purpose)
purpose_options.select_by_index(random.randint(1, len(purpose_options.options)))
selectedPurpose = purpose_options.first_selected_option.text
print(selectedPurpose)


trading = Select(driver.find_element_by_id("revenueMonths"))
trading.select_by_visible_text("6 to 11 months")

submit = driver.find_element_by_id("getFundedPublic").send_keys(Keys.RETURN)



with open("interface.csv", "a", newline= "") as file:
    bot_inputs = csv.writer(file)
    #bot_inputs.writerow(["Amount", "Purpose", "Company Type", "Trading period"])
    bot_inputs.writerow([amount_generator, selectedPurpose])
file.close


    
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






#driver.quit()
