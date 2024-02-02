from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from monitoramento_ambiental.models import Propriedade

class PropriedadeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Propriedade.objects.create(
            nomePropriedade="Propriedade Teste",
            numeroCar="CAR123456",
            uf="UF",
            municipio="Municipio Teste",
            pais="Pais Teste",
            status=True,
            liberado=1
        )

    def test_propriedade_creation(self):
        propriedade = Propriedade.objects.get(idPropriedade=1)
        self.assertEqual(propriedade.nomePropriedade, "Propriedade Teste")
        self.assertEqual(propriedade.numeroCar, "CAR123456")
        self.assertEqual(propriedade.uf, "UF")
        self.assertEqual(propriedade.municipio, "Municipio Teste")
        self.assertEqual(propriedade.pais, "Pais Teste")
        self.assertTrue(propriedade.status)
        self.assertEqual(propriedade.liberado, 1)

class PropriedadeViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.token = RefreshToken.for_user(cls.user)

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        Propriedade.objects.create(
            nomePropriedade="Propriedade Teste",
            numeroCar="CAR123456",
            uf="UF",
            municipio="Municipio Teste",
            pais="Pais Teste",
            status=True,
            liberado=1
        )

    def test_create_propriedade_view(self):
        url = reverse('propriedade-list')
        data = {
            "nomePropriedade": "Nova Propriedade",
            "numeroCar": "CAR654321",
            "uf": "UF Teste",
            "municipio": "Novo Municipio",
            "pais": "Novo Pais",
            "status": True,
            "liberado": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        propriedade = Propriedade.objects.get(numeroCar=data['numeroCar'])
        self.assertEqual(propriedade.nomePropriedade, data['nomePropriedade'])
