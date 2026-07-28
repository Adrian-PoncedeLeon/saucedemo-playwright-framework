
def test_inventory_page_loaded(login_page):
    login_page.navigate()
    inventory_page = login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()

def test_add_product_to_cart(login_page):
    login_page.navigate()
    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    assert inventory_page.add_button_text_changed("Sauce Labs Bolt T-Shirt")

