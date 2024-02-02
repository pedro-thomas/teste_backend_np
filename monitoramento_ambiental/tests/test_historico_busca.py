from django.test import TestCase
from monitoramento_ambiental.models import HistoricoBusca
from django.utils import timezone

class HistoricoBuscaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Assumindo que os campos do modelo estão corretos, o teste deve ser ajustado para usar termo_busca e data_hora_busca
        cls.historico = HistoricoBusca.objects.create(
            termo_busca="Query de teste",
            resultado_busca={"resultado": "algum resultado"}
        )

    def test_historico_busca_query(self):
        self.assertEqual(self.historico.termo_busca, "Query de teste")
