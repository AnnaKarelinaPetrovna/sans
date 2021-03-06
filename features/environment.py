from selenium import webdriver
from app.application import Application
# I imported Application in order to connect it with behave

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='/Users/annakarelina/PycharmProjects/pythonProject/chromedriver')
    # instead of context.driver I will be using context.app + name of the methods that i created for test scripts

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
