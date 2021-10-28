from selenium.webdriver.common.by import By
from behave import given, when, then


# I use open_add_movie method from pages.add_movie page
@given("Open Add Movie page")
def open_add_movie_page(context):
    context.app.add_movie.open_add_movie()


@when("Input valid {title} into title field")
def input_am_title(context, title):
    context.app.add_movie.input_title(title)


@when("Input invalid title {title} into title field")
def input_am_title(context, title):
    context.app.add_movie.input_title(title)


@when("Input valid {data} into data field")
def input_am_data(context, data):
    context.app.add_movie.input_data(data)


@when("Input invalid {data} into data field")
def input_am_data(context, data):
    context.app.add_movie.input_data(data)


@when("Input valid {rating} into rating field")
def input_am_rating(context, rating):
    context.app.add_movie.input_rating(rating)


@when("Input invalid {rating} into rating field")
def input_am_rating(context, rating):
    context.app.add_movie.input_rating(rating)


@then('Message {msg} is shown')
def am_success_msg(context, msg):
    context.app.add_movie.click_add_movie_btn()
    # context.app.add_movie.verify_am_success_msg(msg) since I have not created HTML with a success message instead I
    # have an alert message, so I will create an assertion of the alert text. But the code in line 28 should actually
    # assert success message.

    context.app.add_movie.verify_am_alert(msg)


@then('Error message {msg} is shown')
def am_success_msg(context, msg):
    context.app.add_movie.click_add_movie_btn()
    context.app.add_movie.verify_am_msg(msg), f'The negative tests fails because my page doesn\'t have an error message'
