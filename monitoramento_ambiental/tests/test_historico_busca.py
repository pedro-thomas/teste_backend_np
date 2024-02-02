from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from monitoramento_ambiental.models import HistoricoBusca
from django.utils import timezone
import json

class HistoricoBuscaAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.token = RefreshToken.for_user(cls.user)
        HistoricoBusca.objects.create(
            termo_busca="Termo de Teste",
            resultado_busca=json.dumps({"resultado": "Teste"}),
            data_hora_busca=timezone.now()
        )

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

    def test_list_historico_busca(self):
        url = reverse('historico_buscas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        self.assertEqual(response.data[0]['termo_busca'], "Termo de Teste")
        self.assertTrue("resultado" in json.loads(response.data[0]['resultado_busca']))

