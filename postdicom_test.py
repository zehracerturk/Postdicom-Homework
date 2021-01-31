import unittest
from selenium import webdriver
import time


class TestMainLoginPage(unittest.TestCase):
    # CSS selectors
    errorPopUpText = "#lightbox_container #lightbox_warning_text"
    popUpCloseButtonSelector = "div#lightbox_container button"
    createAccountButtonSelector = "div#login_form_rows_content > button"
    passwordInputSelector = "#pre_sign_up_password"
    emailInputSelector = "#pre_sign_up_email"
    firstNameInputSelector = "#pre_sign_up_name"
    lastNameInputSelector = "#pre_sign_up_surname"
    termsCheckboxSelector = "#sign_up_terms_and_conditions_checkbox"
    successTextSelector = "div#valid_request h1"

    # Uygun kullanıcı bilgileri
    email = "test2@test.com"
    password = "2Wertaa!"
    firstname = "testusername"
    lastname = "testpassword"

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/User/Desktop/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://www.postdicom.com/en/signup")

    def testSignUpForm(self):
        popupCloseButton = self.driver.find_element_by_css_selector(self.popUpCloseButtonSelector)


        createAccountButton = self.driver.find_element_by_css_selector(self.createAccountButtonSelector)
        createAccountButton.click()

        errorBox = self.driver.find_element_by_css_selector(self.errorPopUpText).text
        self.assertEqual(errorBox, "Invalid email address!")
        popupCloseButton.click()
        emailInput = self.driver.find_element_by_css_selector(self.emailInputSelector)
        emailInput.send_keys(self.email)
        createAccountButton.click()

        errorBox = self.driver.find_element_by_css_selector(self.errorPopUpText).text
        self.assertEqual(errorBox, "Invalid password!")
        popupCloseButton.click()
        passwordInput = self.driver.find_element_by_css_selector(self.passwordInputSelector)
        passwordInput.send_keys(self.password)
        createAccountButton.click()
        time.sleep(1)

        errorBox = self.driver.find_element_by_css_selector(self.errorPopUpText).text
        self.assertEqual(errorBox, 'Please fill all blanks!')
        popupCloseButton.click()
        firstNameInput = self.driver.find_element_by_css_selector(self.firstNameInputSelector)
        firstNameInput.send_keys(self.firstname)
        createAccountButton.click()

        errorBox = self.driver.find_element_by_css_selector(self.errorPopUpText).text
        self.assertEqual(errorBox, "Please fill all blanks!")
        popupCloseButton.click()
        lastNameInput = self.driver.find_element_by_css_selector(self.lastNameInputSelector)
        lastNameInput.send_keys(self.lastname)
        createAccountButton.click()

        errorBox = self.driver.find_element_by_css_selector(self.errorPopUpText).text
        self.assertEqual(errorBox, "Please accept Terms & Conditions")
        popupCloseButton.click()
        termsCheckbox = self.driver.find_element_by_css_selector(self.termsCheckboxSelector)
        termsCheckbox.click()
        createAccountButton.click()

        time.sleep(4)
        successText = self.driver.find_element_by_css_selector(self.successTextSelector)
        self.assertEqual(successText, "Your pre-registration was successfully completed.")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()