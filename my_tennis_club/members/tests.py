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
		self.assertTemplateUsed(resp, 'all_members.html')
		self.assertContains(resp, 'Més que un club')

	def test_main_page_renders(self):
		# Arrange
		url = reverse('main')

		# Act
		resp = self.client.get(url)

		# Assert
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'main.html')
		self.assertContains(resp, 'Bienvenidos')

	def test_django_guide_page_renders_and_has_back_button(self):
		# Arrange
		url = reverse('django_guide')

		# Act
		resp = self.client.get(url)

		# Assert
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'myfirst.html')
		self.assertContains(resp, '¿Qué es Django?')
		self.assertContains(resp, 'Volver al Club')

	def test_404_page_when_not_found(self):
		# Forzar 404
		resp = self.client.get('/ruta-inexistente-xyz/')
		self.assertEqual(resp.status_code, 404)
		# Mientras DEBUG esté True Django puede usar su default; handler se prueba con DEBUG False normalmente.
		# Verificamos que contiene código 404 o texto indicativo
		self.assertIn('404', resp.content.decode())
