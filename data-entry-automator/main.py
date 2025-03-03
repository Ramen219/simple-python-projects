import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Load the CSV file
data = pd.read_csv("customer_data.csv")

# Start the WebDriver (e.g., Chrome)
driver = webdriver.Chrome(executable_path="path_to_chromedriver")

# Navigate to the form page (example)
driver.get("https://example.com/form")

for index, row in data.iterrows():
    # Find form fields by their HTML names or IDs
    name_field = driver.find_element_by_name("name")
    email_field = driver.find_element_by_name("email")
    phone_field = driver.find_element_by_name("phone")
    
    # Fill the form fields
    name_field.send_keys(row['name'])
    email_field.send_keys(row['email'])
    phone_field.send_keys(row['phone'])
    
    # Submit the form (if needed)
    submit_button = driver.find_element_by_name("submit")
    submit_button.click()
    
    # Add a delay if needed to avoid overloading the server
    driver.implicitly_wait(2)

# Close the driver after completion
driver.quit()
