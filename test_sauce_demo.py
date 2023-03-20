from selenium.webdriver.common.by import By


class TestSauceDemo:

    def test_login_in_sauce_demo(self, browser):
        browser.get("https://www.saucedemo.com/")
        assert "Swag Labs" in browser.title
        self.username_field = browser.find_element(By.ID, "user-name")
        self.username_field.send_keys("standard_user")
        self.password_field = browser.find_element(By.ID, "password")
        self.password_field.send_keys("secret_sauce")
        self.login_button = browser.find_element(By.ID, "login-button")
        self.login_button.click()
        assert "Products" in browser.page_source

    def test_add_product_backpack(self, browser):
        browser.get("https://www.saucedemo.com/")
        self.username_field = browser.find_element(By.ID, "user-name")
        self.username_field.send_keys("standard_user")
        self.password_field = browser.find_element(By.ID, "password")
        self.password_field.send_keys("secret_sauce")
        self.login_button = browser.find_element(By.ID, "login-button")
        self.login_button.click()
        self.add_to_cart_backpack_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_to_cart_backpack_button.click()
        self.shop_cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        self.shop_cart_button.click()
        assert "Sauce Labs Backpack" in browser.page_source

    def test_remove_product_backpack(self, browser):
        browser.get("https://www.saucedemo.com/")
        self.username_field = browser.find_element(By.ID, "user-name")
        self.username_field.send_keys("standard_user")
        self.password_field = browser.find_element(By.ID, "password")
        self.password_field.send_keys("secret_sauce")
        self.login_button = browser.find_element(By.ID, "login-button")
        self.login_button.click()
        self.add_to_cart_backpack_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_to_cart_backpack_button.click()
        self.shop_cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        self.shop_cart_button.click()
        self.remove_product_button = browser.find_element(By.ID, "remove-sauce-labs-backpack")
        self.remove_product_button.click()
        assert "Sauce Labs Backpack" not in browser.page_source
