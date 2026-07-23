from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_purchase(page):
	"""End-to-end test for purchasing the Sauce Labs Backpack on SauceDemo.

	Flow:
	1. Open login page and authenticate
	2. Verify products page loaded
	3. Add backpack to cart and open cart
	4. Verify backpack present in cart
	5. Checkout, enter customer details, finish order
	6. Verify order success
	"""
	# --- Login ---
	login = LoginPage(page)
	login.open()
	login.login("standard_user", "secret_sauce")

	# --- Products page ---
	products = ProductsPage(page)
	assert products.is_products_page_loaded(), "Products page did not load after login"

	# Add the Sauce Labs Backpack to the cart
	products.add_backpack_to_cart()

	# Open the shopping cart
	products.open_cart()

	# --- Cart page ---
	cart = CartPage(page)
	assert cart.is_cart_page_loaded(), "Cart page did not load"
	assert cart.is_backpack_present(), "Backpack was not found in the cart"

	# Proceed to checkout
	cart.checkout()

	# --- Checkout flow ---
	checkout = CheckoutPage(page)
	assert checkout.is_checkout_step_one_loaded(), "Checkout step one did not load"
	checkout.enter_customer_details("John", "Doe", "12345")
	assert checkout.is_checkout_step_two_loaded(), "Checkout step two did not load"
	checkout.finish_order()

	# Verify order success
	assert checkout.is_order_successful(), "Order was not completed successfully"


