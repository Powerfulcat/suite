import sys
import time
import unittest
from selenium import webdriver


class IWebShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://baidu.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login_in(self):
        driver = self.driver
        driver.add_cookie({"name": "BAIDUID", "value": "7E1242969D55FD9982C8BA198AFE803D:SL=0:NR=10:FG=1"})
        driver.add_cookie({"name": "BDUSS", "value": "XZUenk3N2dEZHNOSVVkZVFhLTZSMWhvTVJlcTlUT0RrfmlKeExmRz"
                                                     "hiSmk4NGRiQUFBQUFBJCQAAAAAAAAAAAEAAADa54Izxd12c8XdaGFw"
                                                     "cHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                                                     "AAAAAAAAAAAAAAAAAAAGJmYFtiZmBbL"})
        driver.refresh()

        user_name = driver.find_element_by_class_name("user-name").text
        try:
            self.assertEqual(user_name, "AAAA")
        except AssertionError:
            now_time = time.strftime("%Y-%m-%d %H_%M_%S")
            err_info = sys.exc_info()

            # driver.get_screenshot_as_file("../Images/%s-%s.png" % (now_time, err_info[1]))
            driver.get_screenshot_as_file('./Images/%s-%s.png' % (now_time, err_info[1]))
            raise


if __name__ == '__main__':
    unittest.main
