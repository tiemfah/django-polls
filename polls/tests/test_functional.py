from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.auth.models import User


class pollTest(LiveServerTestCase):
    USER = 'testUser'
    PASSWORD = 'testPassword'

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.driver.add_argument('--headless')
        super(pollTest, self).setUp()

    def tearDown(self):
        self.driver.close()
        super(pollTest, self).tearDown()

    def test_poll(self):
        self.driver.get(self.live_server_url + '/polls/')
        h1 = self.driver.find_element_by_tag_name('h1')
        self.assertIn('Current Polls', h1.text)

    def test_not_authenticated(self):
        self.driver.get(self.live_server_url)
        h5 = self.driver.find_element_by_tag_name('h5')
        self.assertIn('to vote for a topic', h5.text)

    def test__authenticated(self):
        User.objects.create_user(self.USER, password=self.PASSWORD)
        self.driver.get(self.live_server_url + '/accounts/login')
        self.driver.find_element_by_id(
            "id_username").send_keys(self.USER)
        self.driver.find_element_by_id(
            "id_password").send_keys(self.PASSWORD)
        self.driver.find_element_by_tag_name("button").click()
        self.driver.get(self.live_server_url)
        h5 = self.driver.find_element_by_tag_name('h5')
        self.assertIn('Welcome back, ', h5.text)
