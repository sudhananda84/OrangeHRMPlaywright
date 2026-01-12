import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.mark.validlogin
def test_valid_login(page: Page):
    """Launch, login with valid credentials, verify Dashboard is visible."""
    page.goto(BASE_URL)
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "admin123")
    page.click('button[type="submit"]')
    expect(page.locator("xpath=//h6[text()='Dashboard']")).to_be_visible(timeout=25000)

@pytest.mark.invalidlogin
def test_valid_username_invalid_password(page: Page):
    """Launch, login with valid username and invalid password, verify error shown."""
    page.goto(BASE_URL)
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "wrongpassword")
    page.click('button[type="submit"]')
    expect(page.get_by_text("Invalid credentials")).to_be_visible(timeout=20000)
    print(page.title())

@pytest.mark.invalidlogin
def test_invalid_username_invalid_password(page: Page):
    """Launch, login with valid username and invalid password, verify error shown."""
    page.goto(BASE_URL)
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "wrongpassword")
    page.click('button[type="submit"]')
    expect(page.get_by_text("Invalid credentials")).to_be_visible(timeout=20000)
