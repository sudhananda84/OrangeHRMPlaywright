import pytest
from playwright.sync_api import sync_playwright
import os

# Create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False for debug
        context = browser.new_context()
        yield context
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook captures test failures
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # Access the test function's page object
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            # Attach screenshot to HTML report
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.png(screenshot_path))

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()