from pages.base_page import Page
from selenium.webdriver.common.by import By


class AddMovie(Page):
    # AddMovie inherits base_page generic methods, here I can hardcode it
    # by providing url, arguments, inputs

    TITLE_FIELD = (By.ID, 'title_name')
    DATA_FIELD = (By.ID, 'date_name')
    RATING_FIELD = (By.ID, 'rating_name')
    ADD_MOVIE_BTN = (By.ID, 'add_movie')

    def open_add_movie(self):
        self.open_url("file:///Users/annakarelina/Desktop/SANS%20copy.html")

    def input_title(self, title):
        self.input_text(title, *self.TITLE_FIELD)

    def input_data(self, data):
        self.input_text(data, *self.DATA_FIELD)

    def input_rating(self, rating):
        self.input_text(rating, *self.RATING_FIELD)

    def click_add_movie_btn(self):
        self.click_elem(*self.ADD_MOVIE_BTN)

    # Unfortunately, I have not created a page where after submit success message displays.
    # Instead I created alert with a success message.
    # The negative tests fail because I did not created error message in case of any of the inputs is invalid
    # However there is only one error message for invalid

    def verify_am_msg(self, text, *locator):
        self.verify_text(text, *locator), f'The negative tests fails because my page doesn\'t have an error message'

    def verify_am_alert(self, text):
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        assert alert_text == text, f'Actual alert text is "{alert_text}" but expected alert text should be "{text}"'
