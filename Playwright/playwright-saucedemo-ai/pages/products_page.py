"""
Page Object Model for SauceDemo Products Page
This module contains the ProductsPage class that encapsulates all interactions with the SauceDemo products page.
"""

from playwright.sync_api import Page


class ProductsPage:
    """
    Page Object Model for the SauceDemo products page.

    This class encapsulates all interactions with the SauceDemo products page,
    including adding items to cart, navigating to checkout, and verifying page state.
    It follows the Page Object Model (POM) design pattern for better test maintainability.

    NOTE: This implementation follows Playwright best practices by storing Locator objects
    rather than selector strings. Locators are lazy-evaluated and more efficient when
    reused multiple times throughout a test.
    """

    # SauceDemo application products page URL
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        """
        Initialize the ProductsPage with a Playwright Page object.

        This constructor creates Locator objects for all product and navigation elements.
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

        # Create and store Locator objects for page elements
        # These locators are lazy-evaluated and will only query the DOM when needed

        # Product container locator - used to verify page is loaded
        self.products_container = page.locator("[data-test='inventory-container']")

        # Backpack product specific locators
        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.backpack_remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.backpack_title = page.locator("text=Sauce Labs Backpack")

        # Shopping cart locator - used to navigate to cart
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

        # Cart badge locator - displays number of items in cart
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def is_products_page_loaded(self) -> bool:
        """
        Check if the products page has successfully loaded.

        This method verifies that we are on the products page by checking if the
        products container is visible. This is a good wait condition after login.

        Returns:
            bool: True if the products container is visible, False otherwise
        """
        # Check if the products container is visible on the page
        # This confirms we've successfully logged in and navigated to the inventory page
        try:
            self.products_container.is_visible(timeout=5000)
            return True  # Products page is loaded
        except Exception:
            return False  # Products page failed to load

    def add_backpack_to_cart(self) -> None:
        """
        Add the Sauce Labs Backpack product to the shopping cart.

        This method clicks the "Add to Cart" button for the backpack product,
        which adds it to the user's shopping cart. Uses the stored Locator
        object for efficient element interaction.

        Returns:
            None

        Raises:
            Exception: If the add button is not found or clickable
        """
        # Click the "Add to Cart" button for the Sauce Labs Backpack
        # This uses the stored Locator for efficient interaction
        self.backpack_add_button.click()

    def open_cart(self) -> None:
        """
        Navigate to the shopping cart page.

        This method clicks the shopping cart link in the header, which
        redirects the user to the cart page where they can review their items.
        Uses the stored Locator object for efficient element interaction.

        Returns:
            None

        Raises:
            Exception: If the cart link is not found or clickable
        """
        # Click the shopping cart link to navigate to the cart page
        # This uses the stored Locator for efficient interaction
        self.cart_link.click()

    def get_cart_item_count(self) -> int:
        """
        Get the number of items currently in the shopping cart.

        This method reads the cart badge, which displays the count of items
        in the shopping cart. If the badge is not visible, returns 0.

        Returns:
            int: The number of items in the cart, or 0 if badge is not visible
        """
        # Attempt to get the cart item count from the badge
        # The badge displays a number indicating items in cart
        try:
            badge_text = self.cart_badge.text_content()
            # Convert the badge text to integer
            return int(badge_text) if badge_text else 0
        except Exception:
            # Return 0 if badge is not visible or text cannot be converted to int
            return 0

    def is_backpack_in_cart(self) -> bool:
        """
        Check if the backpack has been added to the cart.

        This method verifies whether the backpack is in the cart by checking
        if the "Remove" button is visible (which only shows if the item is in cart).

        Returns:
            bool: True if the backpack is in the cart, False otherwise
        """
        # Check if the Remove button for backpack is visible
        # If the Remove button is visible, the backpack is in the cart
        try:
            self.backpack_remove_button.is_visible(timeout=1000)
            return True  # Backpack is in the cart
        except Exception:
            return False  # Backpack is not in the cart

