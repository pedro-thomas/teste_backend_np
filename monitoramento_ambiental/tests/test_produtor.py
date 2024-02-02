from django.test import TestCase
from monitoramento_ambiental.models import Produtor

class ProdutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.produtor = Produtor.objects.create(nomeProdutor="Produtor Teste", registroIndividual="12345678901")

    def test_nome_label(self):
        field_label = self.produtor._meta.get_field('nomeProdutor').verbose_name
        self.assertEqual(field_label, 'nomeProdutor')

    def test_cpf_label(self):
        field_label = self.produtor._meta.get_field('registroIndividual').verbose_name
        self.assertEqual(field_label, 'registroIndividual')
