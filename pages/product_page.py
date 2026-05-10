"""Page object model for the product page of the application."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import EXPLICIT_WAIT


class ProductPage:
    """Handles product details and cart addition."""

    # Locators for elements on the product page
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Add to cart')]"
    )

    BUY_NOW_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Buy it now')]"
    )

    SUNSET_VARIANT = (
        By.XPATH,
        "//label[contains(.,'Sunset')]"
    )

    def __init__(self, driver):
        """Initialize the ProductPage with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def verify_product_page(self):
        """Verify that the product page is loaded by checking the Add to Cart button."""
        print("\n[INFO] Verifying product page...")
        add_to_cart = self.wait.until(
            EC.visibility_of_element_located(
                self.ADD_TO_CART_BUTTON
            )
        )

        assert add_to_cart.is_displayed()
        print("[INFO] Product page verified successfully.")

    def select_sunset_variant(self):
        """Select the Sunset variant for the product."""
        print("\n[INFO] Selecting Sunset variant...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.SUNSET_VARIANT
            )
        ).click()
        print("[INFO] Sunset variant selected.")

    def click_add_to_cart(self):
        """Click the Add to Cart button to add the product to the cart."""
        print("\n[INFO] Clicking Add to Cart button...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            )
        ).click()
        print("[INFO] Product added to cart.")