import openai
from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pynput.keyboard import Key, Controller

# Set your OpenAI API key
openai.api_key = "Paste Your OPENAI apikey here"
client = OpenAI(api_key=openai.api_key)

# Function to generate responses using OpenAI API
def generate_response(prompt):
    response = client.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Generate responses for each field
first_name = generate_response("Generate a first name for a form.")
middle_name = generate_response("Generate a middle name for a form.")
last_name = generate_response("Generate a last name for a form.")
address_line1 = generate_response("Generate a small address line 1 for a form.")
address_line2 = generate_response("Generate a small address line 2 for a form.")
city = generate_response("Generate an actual city name for a form.")
state = generate_response("Generate an actual state name for a form.")
postal_code = generate_response("Generate a postal code for a form.")
email = generate_response("Generate a gmail address for a form.")
phone_number = generate_response("Generate a random phone number for a form.")
linkedin = generate_response("Generate a random LinkedIn profile URL for a form.")
ai_interest = generate_response("Describe your interest in AI for a form in just 20 words.")
web_automation = generate_response("Describe your experience in web automation for a form in just 20 words.")
reverse_linkedlist = generate_response("Explain how to reverse a linked list for a form in just 20 words.")
cover_letter = generate_response("Write a precise cover letter content for a form in 30 words")

# Set up the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the webpage
    driver.get("https://form.jotform.com/241617189501153")

    # Fill out the form
    driver.find_element(By.ID, "first_11").send_keys(first_name)  # First Name
    time.sleep(1)
    driver.find_element(By.ID, "middle_11").send_keys(middle_name)    # Middle Name
    time.sleep(1)
    driver.find_element(By.ID, "last_11").send_keys(last_name)    # Last Name
    time.sleep(1)
    driver.find_element(By.ID, "input_16_addr_line1").send_keys(address_line1)  # Address Line 1
    time.sleep(1) 
    driver.find_element(By.ID, "input_16_addr_line2").send_keys(address_line2)    # Address Line 2
    time.sleep(1)
    driver.find_element(By.ID, "input_16_city").send_keys(city)            # City
    time.sleep(1)
    driver.find_element(By.ID, "input_16_state").send_keys(state)                # State
    time.sleep(2)
    driver.find_element(By.ID, "input_16_postal").send_keys(postal_code)            # Postal Code
    time.sleep(2)
    driver.find_element(By.ID, "input_12").send_keys(email)    # Email
    time.sleep(2)
    driver.find_element(By.ID, "input_13_full").send_keys(phone_number)       # Phone Number
    time.sleep(2)
    driver.find_element(By.ID, "input_19").send_keys(linkedin)  # LinkedIn
    time.sleep(2)
    driver.find_element(By.ID, "input_24").send_keys(ai_interest)    # AI Interest
    time.sleep(3)
    driver.find_element(By.ID, "input_25").send_keys(web_automation)  # Web Automation
    time.sleep(3)
    driver.find_element(By.ID, "input_23").send_keys(reverse_linkedlist)  # Reverse LinkedList
    time.sleep(3)
    driver.find_element(By.ID, "input_22").send_keys(cover_letter)  # Cover Letter
    time.sleep(2)

    # Handle file upload
    driver.find_element(By.ID, "cid_17").click()
    time.sleep(5)
    keyboard = Controller()
    keyboard.type("C:\\Users\\DSK 8920444598\\Downloads\\Anurag's Resume V2.pdf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    # Submit the form
    driver.find_element(By.ID, "input_9").click()


    # Print a message to indicate form submission is complete
    print("Form submitted. Check the browser window.")

    # Pause execution to allow for manual review
    input("Press Enter to continue and close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
