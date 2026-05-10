"""Test suite for the complete purchase flow of the AdNabu e-commerce application."""


class TestCompletePurchaseFlow:
    """Test class for verifying the end-to-end purchase flow from search to checkout."""

    def test_search_add_cart_checkout_flow(self, page_objects):
        """Test the complete flow from searching a product to adding it to cart and checkout."""
        print("\n" + "="*60)
        print("[TEST START] Starting complete purchase flow test")
        print("="*60)

        # Unpack page objects from the fixture
        home_page = page_objects['home_page']
        search_page = page_objects['search_page']
        product_page = page_objects['product_page']
        cart_page = page_objects['cart_page']
        checkout_page = page_objects['checkout_page']

        # ---------------------------------------------------
        # Open Application
        # ---------------------------------------------------
        print("\n[STEP 1] Opening Application")
        home_page.open_application(
            "https://adnabu-store-assignment1.myshopify.com"
        )

        # ---------------------------------------------------
        # Enter Password
        # ---------------------------------------------------
        print("\n[STEP 2] Entering Store Password")
        home_page.enter_store_password(
            "AdNabuQA"
        )

        # ---------------------------------------------------
        # List Featured Products
        # ---------------------------------------------------
        print("\n[STEP 3] Listing Featured Products")
        home_page.list_all_products()

        # ---------------------------------------------------
        # Search Product
        # ---------------------------------------------------
        print("\n[STEP 4] Searching for Product")
        home_page.click_search_icon()

        search_page.search_product(
            "the-complete-snowboard"
        )

        search_page.verify_products_section()

        search_page.click_matching_product()

        # ---------------------------------------------------
        # Product Page Actions
        # ---------------------------------------------------
        print("\n[STEP 5] Performing Product Page Actions")
        product_page.verify_product_page()

        product_page.select_sunset_variant()

        product_page.click_add_to_cart()

        # ---------------------------------------------------
        # Cart Actions
        # ---------------------------------------------------
        print("\n[STEP 6] Performing Cart Actions")
        cart_page.verify_cart_drawer_opened()
        cart_page.click_checkout()

        # ---------------------------------------------------
        # Checkout Verification
        # ---------------------------------------------------
        print("\n[STEP 7] Verifying Checkout Page")
        checkout_page.verify_payment_page()
        checkout_page.navigate_back_to_store()

        # ---------------------------------------------------
        # Verify Product In Cart
        # ---------------------------------------------------
        print("\n[STEP 8] Verifying Product in Cart")
        home_page.click_cart_icon()
        cart_page.verify_product_in_cart()
        print("\n" + "="*60)
        print("[TEST END] Complete purchase flow test finished successfully")
        print("="*60)