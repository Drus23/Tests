from selenium import webdriver


def configurate():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "78.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities
    )
    return driver