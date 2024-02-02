from django.test import TestCase
from monitoramento_ambiental.models import Produtor
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from monitoramento_ambiental.models import Produtor

class ProdutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Produtor.objects.create(
            registroIndividual="RI123456",
            nomeProdutor="Nome Produtor Teste",
            status=True
        )

    def test_produtor_creation(self):
        produtor = Produtor.objects.get(idProdutor=1)
        self.assertEqual(produtor.registroIndividual, "RI123456")
        self.assertEqual(produtor.nomeProdutor, "Nome Produtor Teste")
        self.assertTrue(produtor.status)

    def test_produtor_str(self):
        produtor = Produtor.objects.get(idProdutor=1)
        self.assertEqual(str(produtor), produtor.nomeProdutor)

class ProdutorViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.token = RefreshToken.for_user(cls.user)
        cls.produtor = Produtor.objects.create(
            registroIndividual="RI123456",
            nomeProdutor="Nome Produtor Teste",
            status=True
        )

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

    def test_retrieve_produtor(self):
        url = reverse('produtor-detail', args=[self.produtor.idProdutor])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nomeProdutor'], self.produtor.nomeProdutor)

    def test_create_produtor(self):
        url = reverse('produtor-list')
        data = {
            'registroIndividual': "RI654321",
            'nomeProdutor': "Novo Nome Produtor",
            'status': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nomeProdutor'], "Novo Nome Produtor")
        self.assertTrue(response.data['status'])

    def test_list_produtor(self):
        url = reverse('produtor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)