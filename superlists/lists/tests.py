from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve 
from lists.views import home_page 
from django.http import HttpRequest 


# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found=resolve('/')
		self.assertEqual(found.func,home_page)
	def test_home_page_view_returns_html(self):
		request=HttpRequest()
		response=home_page(request)
		'''
		check if returned html file is expected home.html
		decode() converts response.content bytes to unicode string
		'''
		self.assertEqual(response.content.decode(),
			render_to_string('home.html'))

