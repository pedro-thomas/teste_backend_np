from django.test import TestCase
from django.urls import reverse
from monitoramento_ambiental.models import Propriedade

class PropriedadeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração inicial para os testes
        cls.propriedade = Propriedade.objects.create(
            nome='Fazenda Exemplo',
            numero_car='123456789'
        )

    # Testes do Modelo
    def test_model_str(self):
        self.assertEqual(str(self.propriedade), 'Fazenda Exemplo')

    def test_numero_car_length(self):
        max_length = self.propriedade._meta.get_field('numero_car').max_length
        self.assertEqual(max_length, 15)

    # Testes da View
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/monitoramento_ambiental/propriedades/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('propriedade_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('propriedade_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monitoramento_ambiental/propriedade_list.html')
