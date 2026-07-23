"""
Page Object Model for SauceDemo Login Page
This module contains the LoginPage class that encapsulates all interactions with the SauceDemo login page.
"""

from playwright.sync_api import Page


class LoginPage:
    """
    Page Object Model for the SauceDemo login page.

    This class encapsulates all interactions with the SauceDemo login page,
    including navigation, element locators, and login functionality.
    It follows the Page Object Model (POM) design pattern for better test maintainability.

    NOTE: This implementation follows Playwright best practices by storing Locator objects
    rather than selector strings. Locators are lazy-evaluated and more efficient when
    reused multiple times throughout a test.
    """

    # SauceDemo application URL
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page object.

        This constructor creates Locator objects for all form elements.
        By storing Locators instead of selector strings, we follow Playwright best practices:
        - Locators are lazy-evaluated (not queried until actually used)
        - They are more efficient when reused multiple times
        - They provide a cleaner, more readable API for interactions

        Args:
            page (Page): The Playwright Page object for the current browser context.
                        This is the synchronous API Page instance used for all interactions.
        """
        # Store the page object for use in navigation and other page-level operations
        self.page = page

        # Create and store Locator objects for all form elements
        # These locators are lazy-evaluated and will only query the DOM when needed
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self) -> None:
        """
        Navigate to the SauceDemo login page.

        This method opens the SauceDemo application by navigating to the base URL.
        Returns:
            None
        """
        # Navigate to the SauceDemo application
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Perform the login action with provided credentials.

        This method fills in the username and password fields and clicks the login button.
        It uses the Locator objects stored in __init__ for efficient element interactions.

        Args:
            username (str): The username to enter in the username field
            password (str): The password to enter in the password field

        Returns:
            None

        Example:
            >>> login_page.login("standard_user", "secret_sauce")
        """
        # Fill the username field with the provided username using the stored Locator
        # This is more efficient than querying the selector each time
        self.username.fill(username)

        # Fill the password field with the provided password using the stored Locator
        self.password.fill(password)

        # Click the login button using the stored Locator to submit the form
        self.login_button.click()

    def get_error_message(self) -> str:
        """
        Retrieve the error message displayed on the login page.

        This method is useful for validating login failures or other error states.
        Uses the stored Locator object for efficient element interaction.

        Returns:
            str: The text content of the error message element, or empty string if not present
        """
        # Attempt to get the error message text using the stored Locator
        # The Locator has already been created in __init__, so we just use it here
        try:
            error_text = self.error_message.text_content()
            return error_text if error_text else ""
        except Exception:
            # Return empty string if error element is not found or not visible
            return ""

    def is_logged_in(self) -> bool:
        """
        Check if the user has successfully logged in.

        This method verifies the login status by checking if we've been redirected
        away from the login page (i.e., the login button is no longer visible).
        Uses the stored Locator object for efficient element interaction.

        Returns:
            bool: True if the login button is not visible (logged in), False otherwise
        """
        # Check if the login button is visible using the stored Locator
        # If the button is not visible, the user has been redirected to the products page (logged in)
        try:
            self.login_button.is_visible(timeout=1000)
            return False  # Login button still visible, user is not logged in
        except Exception:
            return True  # Login button not visible, user is logged in


