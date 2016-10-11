from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

driver = webdriver.Firefox()
site = "http://www.supremenewyork.com/shop/"
#product = "jackets/v32hlbpev/jpx7dft6y"
product = "accessories/bywoi7gex/jzq68foij"
driver.get(site+product)

preference = ["Large","Medium","XLarge","Small"]
i = 0
sizeField = "//select[@name='size']"

def selectMySize(size):
    sizeWanted = "/option[text()='"+size+"']"
    selectSize = sizeField + sizeWanted
    try:
        sizeWantedElement = driver.find_element_by_xpath(selectSize)
        sizeWantedElement.click()
        return
    except NoSuchElementException:
        print("preferred size not available")
        global i
        i = i + 1
        if i < len(preference):
            selectMySize(preference[i])
        else:
            print("none of your preferred sizes are available")

try:
    sizeFieldElement = driver.find_element_by_xpath(sizeField)
    selectMySize(preference[i])
except NoSuchElementException:
    print("no size field")

addToCartButton = "//input[@name='commit']"

cart = "http://www.supremenewyork.com/shop/cart"

def waitForAdd():
    try:
        inCartField = "//b[@class='button in-cart']"
        driver.find_element_by_xpath(inCartField)
        print("added")
        return
    except NoSuchElementException:
        print("not added")
        waitForAdd();

addToCartElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(addToCartButton)).click()
waitForAdd()

checkout = "https://www.supremenewyork.com/checkout"
driver.get(checkout)

name="Jake Vollkommer"
email="jakexxvollkommer@aol.com"
tel="6317457857"
address="28 Sedgemere Road"
address2=""
zipCode="11934"
city="Center Moriches"
state="NY"
country="USA"
cardType="Visa"
cardNumber="1234123412341234"
expDateMonth="02"
expDateYear="2019"
cvv="688"

nameElement         = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("order_billing_name"))
emailElement        = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("order_email"))
telElement          = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("order_tel"))
addressElement      = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("bo"))
#optional
address2Element     = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("oba3"))
zipElement          = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("order_billing_zip"))
cityElement         = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("order_billing_city"))
cardNumberElement   = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("cnb"))
cvvElement          = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("vval"))

def checkIfHovered():
    try:
        driver.find_element_by_xpath("//div[@class='icheckbox_minimal hover']")
        print("box is hovered")
        return
    except NoSuchElementException:
        print("not hovered yet")
        checkIfHovered()

def checkBox():
    checkboxElementClickarea = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("order_terms"))
    checkboxElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//div[@class='icheckbox_minimal']"))
    hover = ActionChains(driver).move_to_element(checkboxElement)
    hover.perform()
    checkIfHovered()
    checkboxElementClickarea.click()
    print("nice")

checkBox()
driver.find_element_by_xpath("//select[@name='order[billing_state]']/option[text()='"+state+"']").click()
driver.find_element_by_xpath("//select[@name='order[billing_country]']/option[text()='"+country+"']").click()
driver.find_element_by_xpath("//select[@name='credit_card[type]']/option[text()='"+cardType+"']").click()
driver.find_element_by_xpath("//select[@name='credit_card[month]']/option[text()='"+expDateMonth+"']").click()
driver.find_element_by_xpath("//select[@name='credit_card[year]']/option[text()='"+expDateYear+"']").click()

elements    = [nameElement, emailElement, telElement, addressElement, address2Element, zipElement, cityElement, cardNumberElement, cvvElement]
keys        = [name, email, tel, address, address2, zipCode, city, cardNumber, cvv]

for i in range(len(elements)):
    elements[i].clear()
    elements[i].send_keys(keys[i])
