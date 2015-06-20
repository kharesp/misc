from selenium import webdriver
import unittest

class NewVisitorTestCase(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def test_can_make_list_and_retrieve_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish writig TestCase')

if __name__=='__main__':
	unittest.main()	
