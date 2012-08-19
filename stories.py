from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import storyteller


class JoelWantsToExecuteTestsInOrderStory(storyteller.Story):
    @classmethod
    def setUpClass(cls):
        browser = webdriver.Firefox()
        browser.implicitly_wait(5)
        cls.browser = browser

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()

    @storyteller.chapter
    def in_which_joel_goes_to_stack_overflow(self):
        self.browser.get("http://stackoverflow.com/")

    @storyteller.chapter
    def in_which_joel_does_a_search(self):
        search = self.browser.find_element_by_name('q')
        search.send_keys("python unittest execution order")
        search.send_keys(Keys.RETURN)

    @storyteller.chapter
    def in_which_joel_clicks_the_first_result(self):
        self.browser.find_element_by_xpath('//a[@class="question-hyperlink"]').click()

    @storyteller.chapter
    def in_which_joel_finds_the_answer(self):
        answer = self.browser.find_element_by_xpath('//*[@class="vote-accepted-on"]/../../..//*[@class="post-text"]')
        self.assertEquals(answer.text, "Just define the tests in the order you want them to run.")


if __name__ == '__main__':
    storyteller.main()
