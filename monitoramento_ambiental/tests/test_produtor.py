from django.test import TestCase
from monitoramento_ambiental.models import Produtor, AnaliseAutomatica, Propriedade, Vinculo

class ProdutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração inicial para os testes do modelo Produtor
        Produtor.objects.create(nome="Produtor Teste", cpf="12345678901")

    def test_nome_label(self):
        produtor = Produtor.objects.get(id=1)
        field_label = produtor._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')

    def test_cpf_label(self):
        produtor = Produtor.objects.get(id=1)
        field_label = produtor._meta.get_field('cpf').verbose_name
        self.assertEqual(field_label, 'cpf')

class AnaliseAutomaticaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração inicial para os testes do modelo AnaliseAutomatica
        propriedade = Propriedade.objects.create(nome="Propriedade Teste", numero_car="CAR12345")
        produtor = Produtor.objects.create(nome="Produtor Teste", cpf="12345678901")
        Vinculo.objects.create(propriedade=propriedade, produtor=produtor)
        AnaliseAutomatica.objects.create(propriedade=propriedade, status="Liberado")

    def test_status_label(self):
        analise = AnaliseAutomatica.objects.get(id=1)
        field_label = analise._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')
