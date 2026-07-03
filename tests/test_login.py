
def test_login(login_page):
    login_page.navigate()
    inventory_page = login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()


