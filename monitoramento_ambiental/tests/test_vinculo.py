from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from monitoramento_ambiental.models import Propriedade, Produtor, Vinculo

class VinculoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.propriedade = Propriedade.objects.create(
            nomePropriedade="Propriedade Vinculo",
            numeroCar="CAR98765",
            uf="UF Teste",
            municipio="Municipio Teste",
            pais="Pais Teste",
            status=True,
            liberado=1
        )
        cls.produtor = Produtor.objects.create(
            registroIndividual="RI987654",
            nomeProdutor="Nome Produtor Vinculo",
            status=True
        )
        cls.vinculo = Vinculo.objects.create(
            idPropriedade=cls.propriedade,
            idProdutor=cls.produtor
        )

    def test_vinculo_creation(self):
        self.assertEqual(self.vinculo.idPropriedade.nomePropriedade, "Propriedade Vinculo")
        self.assertEqual(self.vinculo.idProdutor.nomeProdutor, "Nome Produtor Vinculo")

    def test_vinculo_str(self):
        expected_str = 'Propriedade Vinculo - Nome Produtor Vinculo'
        self.assertEqual(str(self.vinculo), expected_str)

class VinculoViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.token = RefreshToken.for_user(cls.user)

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        self.propriedade = Propriedade.objects.create(
            nomePropriedade="Propriedade Vinculo",
            numeroCar="CAR98765",
            uf="UF Teste",
            municipio="Municipio Teste",
            pais="Pais Teste",
            status=True,
            liberado=1
        )
        self.produtor = Produtor.objects.create(
            registroIndividual="RI987654",
            nomeProdutor="Nome Produtor Vinculo",
            status=True
        )
        self.vinculo = Vinculo.objects.create(
            idPropriedade=self.propriedade,
            idProdutor=self.produtor
        )

    def test_retrieve_vinculo(self):
        url = reverse('vinculo-detail', args=[self.vinculo.idVinculo])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['idPropriedade']['idPropriedade'], self.propriedade.idPropriedade)
        self.assertEqual(response.data['idProdutor']['idProdutor'], self.produtor.idProdutor)
