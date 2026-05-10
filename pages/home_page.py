"""Page object model for the home page of the application."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import EXPLICIT_WAIT


class HomePage:
    """Handles interactions on the home page."""

    # Locators for elements on the home page
    PASSWORD_INPUT = (By.NAME, "password")

    ENTER_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Enter')]"
    )

    FEATURED_PRODUCTS = (
        By.CSS_SELECTOR,
        "a.full-unstyled-link"
    )

    SEARCH_ICON = (
        By.CSS_SELECTOR,
        "summary.header__icon--search"
    )

    CART_ICON = (
        By.CSS_SELECTOR,
        ".header__icon--cart"
    )

    def __init__(self, driver):
        """Initialize the HomePage with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_application(self, url):
        """Navigate to the application's home page."""
        print(f"\n[INFO] Opening application at: {url}")
        self.driver.get(url)

    def enter_store_password(self, password):
        """Enter the store password and submit to access the site."""
        print(f"\n[INFO] Entering store password...")
        password_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_INPUT
            )
        )

        password_input.send_keys(password)

        self.driver.find_element(
            *self.ENTER_BUTTON
        ).click()
        print("[INFO] Password entered and submitted.")

    def list_all_products(self):
        """Print the names of all featured products on the page."""
        print("\n===== FEATURED PRODUCTS =====")
        all_products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.FEATURED_PRODUCTS
            )
        )

        for product in all_products:

            product_name = product.text.strip()

            if product_name:
                print(product_name)

    def click_search_icon(self):
        """Click the search icon to open the search functionality."""
        print("\n[INFO] Clicking search icon...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_ICON
            )
        ).click()
        print("[INFO] Search icon clicked.")

    def click_cart_icon(self):
        """Click the cart icon to view the shopping cart."""
        print("\n[INFO] Clicking cart icon...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.CART_ICON
            )
        ).click()
        print("[INFO] Cart icon clicked.")