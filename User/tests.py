from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .models import CustomUser
from .views import CustomUserModelViewSet

class TestAuthorViewSet(TestCase):
    def setUp(self) -> None:
        self.name = "admin"
        self.password = "masteradmin"
        self.email = "admin@totonotes.ru"
        self.url = "/api/usersapp/"
        self.admin = CustomUser.objects.create(
            username=self.name,
            password=self.password,
            email=self.email,
            is_superuser=True,
            is_staff=True,
        )

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = CustomUserModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass