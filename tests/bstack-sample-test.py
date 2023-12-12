import pytest
from selenium.webdriver.common.by import By

FIRSTNAME = (By.ID, 'firstNameInput')
LASTNAME = (By.ID, 'lastNameInput')
ADDRESS = (By.ID, 'addressLine1Input')
PROVINCE = (By.ID, 'provinceInput')
POST_CODE= (By.ID, 'postCodeInput')
CHECKOUT_SHIPPING_CONTINUE = (By.ID, 'checkout-shipping-continue')
CHECKOUT_BUTTON = (By.CLASS_NAME, 'optimizedCheckout-buttonSecondary')

def test_example(selenium):
    selenium.get('https://bstackdemo.com/')

    # locating product on webpage and getting name of the product
    productText = selenium.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the 'Add to cart' button
    selenium.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

    # waiting until the Cart pane has been displayed on the webpage
    selenium.find_element(By.CLASS_NAME, 'float-cart__content')

    # locating product in cart and getting name of the product in cart
    productCartText = selenium.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text


    # checking whether product has been added to cart by comparing product name
    assert productCartText == productText

    selenium.find_element(By.CLASS_NAME, 'buy-btn')

    selenium.find_element(FIRSTNAME).send_keys("firstname"+'\n')
    selenium.find_element(FIRSTNAME).send_keys("firstname" + '\n')
    selenium.find_element(FIRSTNAME).send_keys("firstname" + '\n')
    selenium.find_element(FIRSTNAME).send_keys("firstname" + '\n')






