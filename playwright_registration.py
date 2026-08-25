from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    registration_link = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    registration_form_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_form_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_form_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')
    dashboard_toolbar_title_text = page.get_by_test_id('dashboard-toolbar-title-text')

    page.goto(registration_link)
    registration_form_email_input.fill('user.name@gmail.com')
    registration_form_username_input.fill('username')
    registration_form_password_input.fill('password')
    registration_button.click()
    expect(dashboard_toolbar_title_text).to_be_visible()
