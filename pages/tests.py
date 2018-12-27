from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
	def test_home_page(self):		# The name of the functions can be anything
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200) #checking if the status code is a success that is 200

	def test_about_page(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 200)
