
import pytest

@pytest.mark.parametrize(
    "username",
    [
        pytest.param("standard_user", id = "Standard user"),
        pytest.param("problem_user", id = "Problem user"),
        pytest.param("performance_glitch_user", id = "Performance user"),
        pytest.param("error_user", id = "Error user")
    ]
)
def test__valid_login(login_page, username):
    login_page.navigate()
    inventory_page = login_page.login(username, "secret_sauce")
    assert inventory_page.is_loaded()

@pytest.mark.parametrize(
    "username",
    [
        pytest.param("locked_out_user", id = "Locked Out user"),
        pytest.param("invalid_user", id = "Invalid user")
    ]
)
def test__invalid_login(login_page, username):
    login_page.navigate()
    inventory_page = login_page.login(username, "secret_sauce")
    assert not inventory_page.is_loaded()

