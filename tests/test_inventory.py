
def test_inventory_page_loaded(inventory_page):
    assert inventory_page.is_loaded()

def test_add_product_to_cart(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    assert inventory_page.add_button_text_changed("Sauce Labs Bolt T-Shirt")

