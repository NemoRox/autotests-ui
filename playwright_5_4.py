from playwright.sync_api import sync_playwright, expect # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()   # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Проверить наличие элементов: "Email" на экране auth/login
    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()
    # Проверить наличие элементов: "password" на экране auth/login
    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()
    # Проверить наличие элементов: "login button" на экране auth/login
    login_login_button = page.get_by_test_id('login-page-login-button')
    expect(login_login_button).to_be_visible()
    # Нажать на ссылку "Registration", после чего произойдет редирект на страницу Registration
    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.click()
    # Проверить наличие элементов: "Email"
    registration_email_input = page.get_by_test_id('registration-form-username-input')
    expect(registration_email_input).to_be_visible()
    # Проверить наличие элементов: "Password"
    registration_password_input = page.get_by_test_id('registration-form-password-input')
    expect(registration_password_input).to_be_visible()
    # Проверить наличие элементов: "Registration"
    registration_registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_registration_button).to_be_visible()
