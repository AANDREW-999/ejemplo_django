from django.test import TestCase
from django.urls import reverse


class MembersViewTests(TestCase):
	def test_members_page_renders(self):
		# Arrange
		url = reverse('members')

		# Act
		resp = self.client.get(url)

		# Assert
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'myfirst.html')
		# comprueba que renderiza al menos un título de sección
		self.assertContains(resp, '¿Qué es Django?')
