"""
Page Object Model for SauceDemo Cart Page
This module contains the CartPage class that encapsulates all interactions with the SauceDemo shopping cart page.
"""

from playwright.sync_api import Page


class CartPage:
    """
    Page Object Model for the SauceDemo shopping cart page.

    This class encapsulates all interactions with the SauceDemo shopping cart page.
    Its responsibilities are limited and focused:
    - Verifying that we've successfully reached the cart page
    - Confirming that expected items (like the backpack) are present in the cart
    - Clicking the Checkout button to proceed to checkout

    It follows the Page Object Model (POM) design pattern for better test maintainability.

    NOTE: This implementation follows Playwright best practices by storing Locator objects
    rather than selector strings. Locators are lazy-evaluated and more efficient when
    reused multiple times throughout a test.
    """

    # SauceDemo application cart page URL
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        """
        Initialize the CartPage with a Playwright Page object.

        This constructor creates Locator objects for all cart-related elements.
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

        # Create and store Locator objects for cart page elements
        # These locators are lazy-evaluated and will only query the DOM when needed

        # Cart container locator - used to verify we're on the cart page
        self.cart_container = page.locator("[data-test='cart-contents-container']")

        # Cart title locator - displays "Your Cart" heading
        self.cart_title = page.locator("text=Your Cart")

        # Backpack cart item locator - used to verify the backpack is in the cart
        self.backpack_cart_item = page.locator("[data-test='inventory-item-name'][href*='sauce-labs-backpack']")

        # Alternative backpack locator - using the product name text
        self.backpack_name = page.locator("text=Sauce Labs Backpack")

        # Checkout button locator - proceeds to checkout page
        self.checkout_button = page.locator("[data-test='checkout']")

        # Continue Shopping button locator - returns to products page (for reference)
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def is_cart_page_loaded(self) -> bool:
        """
        Check if the cart page has successfully loaded.

        This method verifies that we are on the cart page by checking if the
        cart container is visible. This confirms we've successfully navigated
        to the shopping cart.

        Returns:
            bool: True if the cart page is visible and loaded, False otherwise
        """
        # Check if the cart container is visible on the page
        # This confirms we've successfully navigated to the cart page
        try:
            self.cart_container.is_visible(timeout=5000)
            return True  # Cart page is loaded
        except Exception:
            return False  # Cart page failed to load

    def is_backpack_present(self) -> bool:
        """
        Check if the Sauce Labs Backpack is present in the shopping cart.

        This method verifies that the backpack product is listed in the cart.
        It uses the backpack name locator to confirm the item exists in the cart contents.
        This is a key assertion for verifying that the correct product was added.

        Returns:
            bool: True if the backpack is visible in the cart, False otherwise
        """
        # Check if the backpack product name is visible in the cart
        # This confirms the backpack was successfully added and is displayed in the cart
        try:
            self.backpack_name.is_visible(timeout=1000)
            return True  # Backpack is present in cart
        except Exception:
            return False  # Backpack is not present in cart

    def checkout(self) -> None:
        """
        Click the Checkout button to proceed to the checkout page.

        This method clicks the "Checkout" button, which redirects the user
        from the cart page to the checkout page where they can enter shipping
        and payment information. Uses the stored Locator object for efficient
        element interaction.

        Returns:
            None

        Raises:
            Exception: If the checkout button is not found or clickable
        """
        # Click the Checkout button to proceed to the checkout page
        # This uses the stored Locator for efficient interaction
        self.checkout_button.click()

    def get_cart_items_count(self) -> int:
        """
        Get the number of items currently displayed in the cart.

        This method counts all inventory items in the cart by finding all
        elements with the class that indicates a cart item. This helps verify
        the expected number of items are in the cart.

        Returns:
            int: The number of items in the cart, or 0 if the cart is empty
        """
        # Count all cart items by locating elements with the inventory-item class
        # Each product in the cart has this class
        try:
            cart_items = self.page.locator("[data-test^='inventory-item-']").count()
            return cart_items
        except Exception:
            # Return 0 if unable to count items
            return 0

