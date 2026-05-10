"""Browser driver setup utility."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    """Create and return a configured Chrome WebDriver instance."""

    # Configure Chrome browser options before launching the driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Install the Chrome driver automatically and start a new browser session
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Apply a default implicit wait to allow elements time to appear
    driver.implicitly_wait(5)

    return driver