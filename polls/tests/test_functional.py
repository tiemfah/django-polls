from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class pollTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        # self.driver.add_argument('--headless')
        super(pollTest, self).setUp()

    def tearDown(self):
        self.driver.close()
        super(pollTest, self).tearDown()

    def test_poll(self):
        self.driver.get(self.live_server_url + '/polls/')
        h1 = self.driver.find_element_by_tag_name('h1')
        self.assertIn('Please', h1.text)
