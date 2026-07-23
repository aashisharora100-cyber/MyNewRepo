"""
Pytest Configuration and Fixtures for Playwright SauceDemo Tests
This module contains shared fixtures used across all test files.
"""

import pytest
from typing import Generator, Any
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def page() -> Generator[Page, Any, None]:
    """
    Pytest fixture that provides a Playwright Page object for tests.

    This fixture:
    - Launches a Chromium browser in headless mode
    - Creates a browser context for isolating test sessions
    - Creates a new page for the test
    - Yields the page to the test function
    - Automatically closes the context and browser after the test completes

    This ensures proper cleanup and isolation between tests.

    Returns:
        Page: A Playwright synchronous API Page object ready for test interactions

    Yields:
        Page object to the test function
    """
    # Start the Playwright synchronous API context manager
    with sync_playwright() as p:
        # Launch Chromium browser in headless mode for faster, automated testing
        # Set headless=False to see the browser window during test execution (useful for debugging)
        browser = p.chromium.launch(headless=False,
                                    slow_mo=500)

        # Create a browser context for this test session
        # Contexts are isolated, allowing multiple tests to run independently
        context = browser.new_context()

        # Create a new page within the context
        # Each page represents a single tab in the browser
        test_page = context.new_page()

        # Yield the page to the test function
        # The test can now use this page object for all interactions
        yield test_page

        # Cleanup after test completes
        # Close the browser context (closes all pages within it)
        context.close()

        # Close the browser instance
        browser.close()


