from selenium import webdriver
from channels.testing import ChannelsLiveServerTestCase
from django.contrib.auth.models import User


class ChatTest(ChannelsLiveServerTestCase):

    def setUp(self):
        # Create users on db
        User.objects.create_user(username='user1', password='password123')
        User.objects.create_user(username='user2', password='password123')

        # Open 2 browser instances
        self.browser1 = webdriver.Chrome()
        self.browser2 = webdriver.Chrome()

    def tearDown(self):
        self.browser1.quit()
        self.browser2.quit()

    def test_chat_between_two_users(self):
        # Open webchat of the 2 users
        self.browser1.get(self.live_server_url + "/webchat/")
        self.browser2.get(self.live_server_url + "/webchat/")

        # Authentication of first user
        username_input1 = self.browser1.find_element('id', "id_username")
        password_input1 = self.browser1.find_element('id', 'id_password')
        username_input1.send_keys("user1")
        password_input1.send_keys("password123")
        self.browser1.find_element('xpath', "//button[@type='submit']").click()

        # Authentication of second user
        username_input2 = self.browser2.find_element('id', "id_username")
        password_input2 = self.browser2.find_element('id', 'id_password')
        username_input2.send_keys("user2")
        password_input2.send_keys("password123")
        self.browser2.find_element('xpath', "//button[@type='submit']").click()

        # User1 writes a message
        msg1 = "Ciao da user1!"
        username_input1 = self.browser1.find_element('id', 'messaggio').send_keys(msg1)
        send_button1 = self.browser1.find_element('id', 'messaggio_invia_button')
        send_button1.click()

        for browser in (self.browser1, self.browser2):
            div_messaggi = browser.find_elements('xpath', "//div[@id='webchat_discussione']/div")
            self.assertEqual(div_messaggi[-1].text, "user1 : " + msg1)

        # User2 answers
        msg2 = "Ciao da user2!"
        username_input2 = self.browser2.find_element('id', 'messaggio').send_keys(msg2)
        send_button2 = self.browser2.find_element('id', 'messaggio_invia_button')
        send_button2.click()

        for browser in (self.browser1, self.browser2):
            div_messaggi = browser.find_elements('xpath', "//div[@id='webchat_discussione']/div")
            self.assertEqual(div_messaggi[-1].text, "user1 : " + msg1)

