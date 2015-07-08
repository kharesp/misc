from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys 

class NewVisitorTestCase(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def test_can_make_list_and_retrieve_later(self):
		#check if browser title has To-Do
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do',self.browser.title)
		
		#check if header h1 has To-Do
		header_text=self.browser.find_element_by_tag_name('h1').text 
		self.assertIn('To-Do',header_text)

		#check if there is an input box with default text: Enter a To-Do item
		input_box=self.browser.find_element_by_id('id_new_item')
		self.assertEqual(input_box.get_attribute('placeholder'),
			'Enter a To-Do item')

		#enter first To-Do item and press ENTER
		input_box.send_keys("Item 1")
		input_box.send_keys(Keys.ENTER) 

		#check if To-Do item got added to the table of all To-Do items 
		table=self.browser.find_element_by_id('id_list_table')
		rows=table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text=="Item 1" for row in rows),
			"New item did not appear in table")
		
		#check if there is another input box for adding more To-Do items 
		self.fail('Finish the test')
		
if __name__=='__main__':
	unittest.main()	
