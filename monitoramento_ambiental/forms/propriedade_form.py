from django import forms
from monitoramento_ambiental.models.propriedade import Propriedade

class PropriedadeForm(forms.ModelForm):
    LIBERADO_CHOICES = [
        (0, 'Bloqueado'),
        (1, 'Liberado'),
        (2, 'Alerta'),
    ]

    liberado = forms.ChoiceField(choices=LIBERADO_CHOICES, required=True, label="Estado de Liberação")

    class Meta:
        model = Propriedade
        fields = ['nomePropriedade', 'numeroCar', 'uf', 'municipio', 'pais', 'status', 'liberado']
   
    def __init__(self, *args, **kwargs):
        super(PropriedadeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'