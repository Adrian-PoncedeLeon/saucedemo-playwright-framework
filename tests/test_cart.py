def test_product_added_to_cart(login_page):
    login_page.navigate()
    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    cart_page = inventory_page.go_to_cart()

    assert cart_page.is_loaded()
    assert cart_page.product_exists("Sauce Labs Bolt T-Shirt")