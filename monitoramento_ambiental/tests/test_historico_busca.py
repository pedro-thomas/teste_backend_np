from django.test import TestCase
from django.urls import reverse
from monitoramento_ambiental.models import HistoricoBusca
from monitoramento_ambiental.models import Propriedade
from monitoramento_ambiental.models import Produtor
from django.utils import timezone

class HistoricoBuscaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.propriedade = Propriedade.objects.create(nome="Propriedade Historico", numero_car="CAR67890")
        cls.produtor = Produtor.objects.create(nome="Produtor Historico", cpf="98765432101")
        cls.historico = HistoricoBusca.objects.create(
            query="Query de teste",
            propriedade=cls.propriedade,
            produtor=cls.produtor,
            data_busca=timezone.now()
        )

    def test_historico_busca_query(self):
        self.assertEqual(self.historico.query, "Query de teste")

    def test_historico_busca_relations(self):
        self.assertEqual(self.historico.propriedade.nome, "Propriedade Historico")
        self.assertEqual(self.historico.produtor.nome, "Produtor Historico")

    def test_historico_busca_data(self):
        # Este teste verificará se a data_busca está dentro de um intervalo esperado (por exemplo, hoje)
        today = timezone.now().date()
        self.assertEqual(self.historico.data_busca.date(), today)
