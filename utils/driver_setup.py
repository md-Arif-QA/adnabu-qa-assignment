"""Utility for setting up the browser driver."""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Increased from 10 to 30 seconds for slower machines
EXPLICIT_WAIT = 30


def get_driver():
    """Create and return a configured Chrome WebDriver instance."""

    # Configure Chrome browser options before launching the driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # If running in GitHub Actions CI, we MUST run Chrome in headless mode
    # and add a few specific arguments for headless Linux environments
    if os.environ.get("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    # Since Selenium 4.6.0+, Selenium Manager is built-in.
    # We no longer need `webdriver_manager` which is causing the Exec format error
    # by incorrectly targeting 'THIRD_PARTY_NOTICES.chromedriver'.
    driver = webdriver.Chrome(options=options)

    # Apply a default implicit wait to allow elements time to appear
    driver.implicitly_wait(5)

    return driver
