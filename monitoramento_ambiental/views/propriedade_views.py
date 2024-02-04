from rest_framework import viewsets
from ..models.propriedade import Propriedade
from ..models.historico_busca import HistoricoBusca 
from ..serializers.propriedade_serializer import PropriedadeSerializer
from ..serializers.historico_busca_serializer import HistoricoBuscaSerializer
from django.utils import timezone
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404, render, redirect
from monitoramento_ambiental.forms.propriedade_form import PropriedadeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect



class PropriedadeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PropriedadeSerializer

    def get_queryset(self):
        numero_car = self.request.query_params.get('numero_car', None)
        if numero_car is not None:
            queryset = Propriedade.objects.filter(numeroCar=numero_car)

            HistoricoBusca.objects.create(
                termo_busca=numero_car,
                data_hora_busca=timezone.now(),
                resultado_busca=self.serialize_queryset(queryset)
            )
            return queryset

        return Propriedade.objects.all()

    def serialize_queryset(self, queryset):
        serializer = PropriedadeSerializer(queryset, many=True)
        return serializer.data

class PropriedadeUpdateView(generics.UpdateAPIView):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer

    def patch(self, request, *args, **kwargs):
        propriedade_id = kwargs.get('pk')
        try:
            propriedade = Propriedade.objects.get(pk=propriedade_id)
            propriedade.liberado = request.data.get('liberado', propriedade.liberado)
            propriedade.save()
            return Response({"status": "success", "data": PropriedadeSerializer(propriedade).data}, status=status.HTTP_200_OK)
        except Propriedade.DoesNotExist:
            return Response({"status": "error", "message": "Propriedade não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
def listar_propriedades(request):
    propriedades = Propriedade.objects.all()
    return render(request, '../templates/propriedades/listar_propriedades.html', {'propriedades': propriedades})

def detalhes_propriedade(request, id):
    propriedade = get_object_or_404(Propriedade, pk=id)
    return render(request, '../templates/propriedades/detalhes_propriedade.html', {'propriedade': propriedade})

@login_required
def editar_propriedade(request, pk):
    propriedade = get_object_or_404(Propriedade, pk=pk)
    if request.method == "POST":
        form = PropriedadeForm(request.POST, instance=propriedade)
        if form.is_valid():
            form.save()
            return redirect('detalhes_propriedade', pk=propriedade.pk)
    else:
        form = PropriedadeForm(instance=propriedade)
    return render(request, 'propriedades/editar_propriedade.html', {'form': form})

@login_required
def buscar_por_sicar(request):
    numero_car = request.GET.get('q')  # Alterado para capturar o parâmetro 'q' da URL
    if numero_car:
        propriedades = Propriedade.objects.filter(numeroCar=numero_car)
        if propriedades.exists():
            propriedade = propriedades.first()
            HistoricoBusca.objects.create(
                termo_busca=numero_car,
                data_hora_busca=timezone.now(),
                resultado_busca=f"Propriedade {propriedade.nomePropriedade} encontrada."
            )
            return HttpResponseRedirect(reverse('detalhes_propriedade', args=[propriedade.pk]))
        else:
            HistoricoBusca.objects.create(
                termo_busca=numero_car,
                data_hora_busca=timezone.now(),
                resultado_busca="Nenhuma propriedade encontrada."
            )
            return redirect('listar_propriedades')
    else:
        return redirect('listar_propriedades')