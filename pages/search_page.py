"""Page object model for the search page of the application."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    """Represents the search page with methods to perform searches and interact with results."""

    # Locators for elements on the search page
    SEARCH_BOX = (
        By.NAME,
        "q"
    )

    PRODUCTS_HEADING = (
        By.ID,
        "predictive-search-products"
    )

    MATCHED_PRODUCT = (
        By.XPATH,
        "//p[contains(text(),'The Complete Snowboard')]"
    )

    def __init__(self, driver):
        """Initialize the SearchPage with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def search_product(self, product_name):
        """Enter the product name into the search box."""
        print(f"\n[INFO] Searching for product: {product_name}")
        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        search_box.clear()
        search_box.send_keys(product_name)
        print("[INFO] Product name entered in search box.")

    def verify_products_section(self):
        """Verify that the products section heading is displayed correctly."""
        print("\n[INFO] Verifying products section heading...")
        heading = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCTS_HEADING
            )
        )

        assert heading.text == "PRODUCTS"
        print("[INFO] Products section heading verified successfully.")

    def click_matching_product(self):
        """Click on the matching product in the search results."""
        print("\n[INFO] Clicking on matching product...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.MATCHED_PRODUCT
            )
        ).click()
        print("[INFO] Matching product clicked.")