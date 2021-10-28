class Page:

    # this is the  base page that contains the most common methods used in test scripts

    def __init__(self, driver):
        self.driver = driver

    # generic method to open url
    def open_url(self, url):
        self.driver.get(url)

    def click_elem(self, *locator):
        self.driver.find_element(*locator).click()

    # generic method for inputs that can also be hardcoded in the add_movie page
    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    # verify text is present in url, I did not used it in my current example for add movie functionality
    def verify_text_url(self, text):
        assert text in self.driver.current_url, f'{self.driver.current_url} does not contain expected text {text}'

    # this method is for the message that appears after movie has been successfully added
    # to the catalogue

    def verify_text(self, text, *locator):
        assert text == self.driver.find_element(*locator).text

