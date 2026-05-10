"""Page object model for the checkout page of the application."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Represents the checkout page with methods to verify payment details and navigate back."""

    # Locators for elements on the checkout page
    PAYMENT_HEADING = (
        By.XPATH,
        "//h2[contains(text(),'Payment')]"
    )

    STORE_LINK = (
        By.XPATH,
        "//a[contains(@href,'adnabu-store-assignment1.myshopify.com')]"
    )

    def __init__(self, driver):
        """Initialize the CheckoutPage with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def verify_payment_page(self):
        """Verify that the payment page is loaded and contains all necessary sections."""
        print("\n[INFO] Verifying payment page...")
        payment_heading = self.wait.until(
            EC.visibility_of_element_located(
                self.PAYMENT_HEADING
            )
        )

        assert payment_heading.is_displayed()

        important_texts = [
            "Contact",
            "Delivery",
            "Payment",
            "Credit card",
            "Finalize order",
            "Order summary"
        ]

        page_source = self.driver.page_source

        for text in important_texts:
            assert text in page_source

        print("\nPayment page verified successfully")

    def navigate_back_to_store(self):
        """Click the link to navigate back to the store homepage."""
        print("\n[INFO] Navigating back to store...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.STORE_LINK
            )
        ).click()
        print("[INFO] Navigated back to store.")