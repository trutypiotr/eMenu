import tempfile

from django.urls import reverse
from rest_framework.test import APITestCase
from api.views import MenuViewSet
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from model_bakery import baker
from PIL import Image


class MenuViewSetTestCase(APITestCase):
    list_url = reverse('menus-list')

    post_data = {
        "name": "Menu1",
        "description": "Opis1",
        "dishes": [
            {
                "name": "Danie1",
                "description": "Opis1",
                "price": "3.99",
                "preparation_time": "01:00:00",
                "vegetarian": True
            }
        ]
    }

    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@test.com', password='test123')
        self.menu = baker.make('api.Dish').menu
        self.token = Token.objects.create(user=self.user)

    def test_menus_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_menus_detail_retrieve(self):
        response = self.client.get(reverse('menus-detail', kwargs={'pk': self.menu.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.menu.name)

    def test_menus_create_unauthenticated(self):
        response = self.client.post(self.list_url, self.post_data)
        self.assertEqual(response.status_code, 401)

    def test_menus_create_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.list_url, self.post_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Menu1')


class DishImageViewSetTestCase(APITestCase):
    def setUp(self):
        self.dish = baker.make('api.Dish')

    def test_image_upload(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        response = self.client.patch(reverse('image-detail', kwargs={'pk': self.dish.pk}), format='multipart')

        self.assertEqual(response.status_code, 200)
