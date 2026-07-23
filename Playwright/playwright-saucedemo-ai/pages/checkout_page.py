"""
Page Object Model for SauceDemo Checkout Page
This module contains the CheckoutPage class that encapsulates all interactions with the SauceDemo checkout page.
"""

from playwright.sync_api import Page


class CheckoutPage:
    """
    Page Object Model for the SauceDemo checkout page.

    This class encapsulates all interactions with the SauceDemo checkout pages.
    It handles both checkout step one (customer details) and checkout step two (order review).

    Responsibilities:
    - Entering customer details (first name, last name, postal code)
    - Proceeding to the order review page
    - Completing the order
    - Verifying order success

    NOTE: This implementation follows Playwright best practices by storing Locator objects
    rather than selector strings. Locators are lazy-evaluated and more efficient when
    reused multiple times throughout a test.
    """

    # SauceDemo application checkout page URLs
    CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    CHECKOUT_STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
    CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        """
        Initialize the CheckoutPage with a Playwright Page object.

        This constructor creates Locator objects for all checkout form elements.
        By storing Locators instead of selector strings, we follow Playwright best practices:
        - Locators are lazy-evaluated (not queried until actually used)
        - They are more efficient when reused multiple times
        - They provide a cleaner, more readable API for interactions

        Args:
            page (Page): The Playwright Page object for the current browser context.
        """
        # Store the page object for navigation and page-level operations
        self.page = page

        # Checkout Step One - Customer Details Form Locators
        # These locators target the form fields where users enter shipping information
        self.first_name_field = page.locator("[data-test='firstName']")
        self.last_name_field = page.locator("[data-test='lastName']")
        self.postal_code_field = page.locator("[data-test='postalCode']")

        # Continue button - proceeds from step one to step two (order review)
        self.continue_button = page.locator("[data-test='continue']")

        # Checkout Step Two - Order Review Page Locators
        # Finish button - completes the order purchase
        self.finish_button = page.locator("[data-test='finish']")

        # Order completion confirmation locators
        # Success message displayed after order completes
        self.order_success_message = page.locator("text=Thank you for your order!")

        # Pony Express message - appears on checkout complete page
        self.pony_express_message = page.locator("text=Pony Express")

        # Checkout complete container - verifies we're on the success page
        self.checkout_complete_container = page.locator("[data-test='checkout-complete-container']")

    def enter_customer_details(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Enter customer shipping details in the checkout form.

        This method fills in the first name, last name, and postal code fields
        on checkout step one, then clicks Continue to proceed to step two.
        Uses stored Locator objects for efficient element interaction.

        Args:
            first_name (str): Customer's first name
            last_name (str): Customer's last name
            postal_code (str): Customer's postal code

        Returns:
            None

        Raises:
            Exception: If any form field is not found or clickable
        """
        # Fill the first name field with the provided first name
        self.first_name_field.fill(first_name)

        # Fill the last name field with the provided last name
        self.last_name_field.fill(last_name)

        # Fill the postal code field with the provided postal code
        self.postal_code_field.fill(postal_code)

        # Click the Continue button to proceed to checkout step two (order review)
        self.continue_button.click()

    def finish_order(self) -> None:
        """
        Complete the order by clicking the Finish button.

        This method clicks the Finish button on checkout step two, which
        submits the order and redirects to the order confirmation page.
        Uses the stored Locator object for efficient element interaction.

        Returns:
            None

        Raises:
            Exception: If the finish button is not found or clickable
        """
        # Click the Finish button to complete the order purchase
        # This submits the order and triggers the success page
        self.finish_button.click()

    def is_order_successful(self) -> bool:
        """
        Verify that the order was completed successfully.

        This method checks multiple indicators that the order completed successfully:
        1. The checkout complete container is visible
        2. The success message is displayed
        This provides a robust check that we've reached the order confirmation page.

        Returns:
            bool: True if the order was successful, False otherwise
        """
        # Check if the checkout complete container is visible
        # This confirms we're on the checkout complete page
        try:
            self.checkout_complete_container.is_visible(timeout=5000)
            # Also verify the success message is present
            self.order_success_message.is_visible(timeout=1000)
            return True  # Order completed successfully
        except Exception:
            return False  # Order did not complete successfully

    def is_checkout_step_one_loaded(self) -> bool:
        """
        Verify that checkout step one (customer details) page is loaded.

        This method checks if the first name field is visible, confirming
        that the checkout form is ready for input.

        Returns:
            bool: True if checkout step one is loaded, False otherwise
        """
        # Check if the first name field is visible
        # This confirms the checkout form is ready for customer input
        try:
            self.first_name_field.is_visible(timeout=5000)
            return True  # Checkout step one is loaded
        except Exception:
            return False  # Checkout step one failed to load

    def is_checkout_step_two_loaded(self) -> bool:
        """
        Verify that checkout step two (order review) page is loaded.

        This method checks if the Finish button is visible, confirming
        that the order review page is ready for order completion.

        Returns:
            bool: True if checkout step two is loaded, False otherwise
        """
        # Check if the Finish button is visible
        # This confirms the order review page is loaded and ready
        try:
            self.finish_button.is_visible(timeout=5000)
            return True  # Checkout step two is loaded
        except Exception:
            return False  # Checkout step two failed to load

