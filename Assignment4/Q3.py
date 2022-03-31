# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# inherit TestCase Class and create a new test class
class PythonOrgSearch(unittest.TestCase):

	# initialization of webdriver
	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/srain/Downloads/chromedriver.exe')

	# Test case method. It should always start with test_
	def test_search(self):
		self.driver.get('https://www.google.com')

		# assertion to confirm if title has google keyword in it
		self.assertIn("Google", self.driver.title)

	# cleanup method called after every test performed
	def tearDown(self):
		self.driver.close()

# execute the script
if __name__ == "__main__":
	unittest.main()
