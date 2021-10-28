from pages.add_movie import AddMovie

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.add_movie = AddMovie(self.driver)
