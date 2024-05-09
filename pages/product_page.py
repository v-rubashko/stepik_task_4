from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_messages(self):
        self.should_be_name_message()
        self.should_be_price_message()

    def should_be_name_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_MESSAGE), "No add to basket message"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_NAME).text, "The name of the product and the name product added to the basket do not match"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), "No basket price message"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE).text, "The price of the product and the price product added to the basket do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_PRODUCT_MESSAGE), "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_PRODUCT_MESSAGE), "Success message is not disappeared"
