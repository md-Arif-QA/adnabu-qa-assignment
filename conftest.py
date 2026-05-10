"""Pytest fixtures for the test suite."""

import pytest
from utils.driver_setup import get_driver


@pytest.fixture(scope="function")
def driver():
    """Fixture to provide a configured Chrome WebDriver instance."""
    driver = get_driver()
    yield driver
    # Teardown: close the browser after the test
    driver.quit()


@pytest.fixture(scope="function")
def page_objects(driver):
    """Fixture to provide initialized page objects."""
    from pages.home_page import HomePage
    from pages.search_page import SearchPage
    from pages.product_page import ProductPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    return {
        'home_page': HomePage(driver),
        'search_page': SearchPage(driver),
        'product_page': ProductPage(driver),
        'cart_page': CartPage(driver),
        'checkout_page': CheckoutPage(driver)
    }