import time
import unittest
from selenium import webdriver
from time import sleep
import sys


class IwebShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        url = "https://baidu.com/"
        self.driver.get(url)  # 必须在一开始打开URL后再对浏览器进行设置
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    def test_login_in(self):
        sleep(3)
        driver = self.driver
        driver.add_cookie({"name": "BAIDUID", "value": "7E1242969D55FD9982C8BA198AFE803D:SL=0:NR=10:FG=1"})
        driver.add_cookie({"name": "BDUSS", "value": "XZUenk3N2dEZHNOSVVkZVFhLTZSMWhvTVJlcTlUT0RrfmlKeExmRz"
                                                     "hiSmk4NGRiQUFBQUFBJCQAAAAAAAAAAAEAAADa54Izxd12c8XdaGFw"
                                                     "cHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                                                     "AAAAAAAAAAAAAAAAAAAGJmYFtiZmBbL"})
        driver.refresh()
        # 判断用户名是否一致
        user_name = driver.find_element_by_class_name("user-name").text
        try:
            self.assertEqual(user_name, "happy")
        except AssertionError:
            now_time = time.strftime("%Y-%m%d %H_%M_%S")
            exc_info = sys.exc_info()
            driver.get_screenshot_as_file("./Images/%s-%s.png" % (now_time, exc_info[1]))
            raise


if __name__ == '__main__':
    unittest.main
