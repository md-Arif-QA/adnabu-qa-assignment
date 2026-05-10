"""Page object model for the cart page of the application."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Represents the cart page with methods to verify cart contents and proceed to checkout."""

    # Locators for elements on the cart page
    SUBTOTAL_HEADING = (
        By.XPATH,
        "//h2[contains(text(),'Subtotal')]"
    )

    CART_ICON = (
        By.CSS_SELECTOR,
        ".header__icon--cart"
    )

    PLUS_BUTTON = (
        By.XPATH,
        "//button[@name='plus']"
    )

    SUBTOTAL_VALUE = (
        By.CSS_SELECTOR,
        "p.totals__subtotal-value"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "CartDrawer-Checkout"
    )

    CART_PRODUCT = (
        By.XPATH,
        "//a[contains(text(),'The Complete Snowboard')]"
    )

    def __init__(self, driver):
        """Initialize the CartPage with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def verify_cart_drawer_opened(self):
        """Verify that the cart drawer is opened by checking the subtotal heading."""
        print("\n[INFO] Verifying cart drawer is opened...")
        try:
            subtotal = self.wait.until(
                EC.visibility_of_element_located(
                    self.SUBTOTAL_HEADING
                )
            )
        except TimeoutException:
            print("[WARN] Cart drawer not visible, clicking cart icon to open it...")
            self.open_cart_drawer()
            subtotal = self.wait.until(
                EC.visibility_of_element_located(
                    self.SUBTOTAL_HEADING
                )
            )

        assert subtotal.is_displayed()
        print("[INFO] Cart drawer verified as opened.")

    def open_cart_drawer(self):
        """Open the cart drawer by clicking the cart icon in the header."""
        print("[INFO] Opening cart drawer via header cart icon...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.CART_ICON
            )
        ).click()
        print("[INFO] Cart drawer opened.")

    def click_checkout(self):
        """Click the checkout button to proceed to the checkout page."""
        print("\n[INFO] Clicking checkout button...")
        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        ).click()
        print("[INFO] Checkout button clicked.")

    def verify_product_in_cart(self):
        """Verify that the specific product is present in the cart."""
        print("\n[INFO] Verifying product in cart...")
        product = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_PRODUCT
            )
        )

        assert product.is_displayed()
        print("[INFO] Product verified in cart.")