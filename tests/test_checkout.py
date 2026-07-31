def test_checkout_flow(inventory_page):
    
    assert inventory_page.is_loaded()

    inventory_page.add_to_cart("Sauce Labs Bike Light")
    cart_page = inventory_page.go_to_cart()

    assert cart_page.is_loaded()

    checkout_page1 = cart_page.click_checkout_button()

    assert checkout_page1.is_loaded()

    checkout_page1.fill_information("testname", "testlastname", "12355")
    checkout_page2 = checkout_page1.click_continue_button()

    assert checkout_page2.is_loaded()

    checkout_page3 = checkout_page2.click_finish_button()

    assert checkout_page3.is_loaded()

    inventory_page = checkout_page3.click_back_home_button()

    assert inventory_page.is_loaded()

  
