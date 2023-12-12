import pytest
import time
from dotenv import load_dotenv
import sys
sys.path.insert(0, '/Users/venky.webhook/Projects/pytest-browserstack')
from page.loginPage import LoginPage
from page.homePage import HomePage
from page.checkoutPage import CheckoutPage
from page.orderConfirmation import OrderConfirmationPage
from page.orders import OrdersPage



load_dotenv()


@pytest.mark.nondestructive
@pytest.mark.parametrize(
    "user_name,password",
    [("demouser", "testingisfun99"), ("fav_user", "testingisfun99")])
def test_e2e(selenium, user_name, password):
    base_url="https://bstackdemo.com/"
    login = LoginPage(selenium)
    login.open_base_url(base_url)
    #login.sign_in("fav_user","testingisfun99")
    login.sign_in(user_name,password)
    home = HomePage(selenium)
    home.add_elements_to_cart()
    home.click_buy()
    checkout = CheckoutPage(selenium)
    checkout.enterFirstName('firstname')
    checkout.enterLastName('lastname')
    checkout.enterAddressLine('address')
    checkout.enterProvince('state')
    checkout.enterPostCode('12345')
    checkout.click_on_checkout()
    order_confirm = OrderConfirmationPage(selenium)
    order_confirm.wait_for_confirmation_message()
    order_confirm.click_download_pdf()
    order_confirm.download_exists(selenium, 'confirmation.pdf' )
    order_confirm.click_continue_shopping()
    home.navigate_to_orders()
    orders = OrdersPage(selenium)
    status = orders.verify_orders_placed()
    time.sleep(5)

            