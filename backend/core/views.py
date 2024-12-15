from django.shortcuts import render
from django.http import JsonResponse
from core.models import Processo, Usuario, Material
from django.db.models import Q
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from openpyxl import Workbook
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from core.serializers import UsuarioSerializer, MaterialSerializer

def home(request):
    return render(request, '/')  # Ou qualquer template que você tenha

def pesquisa_material(request):
    query = request.GET.get('q', '')  # Pegamos a pesquisa da URL (ex: /pesquisa/?q=material)
    
    if query:
        materiais = Material.objects.filter(Q(nome__icontains=query) | Q(serial__icontains=query))
    else:
        materiais = Material.objects.all()

    resultados = [
        {
            "nome": material.nome,
            "serial": material.serial,
            "tipo": material.tipo,
        }
        for material in materiais
    ]
    return JsonResponse({"resultados": resultados})

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


#pdf
def gerar_relatorio_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
    p = canvas.Canvas(response)

    processos = Processo.objects.all().order_by("material", "data_inicio")
    p.drawString(100, 800, "Relatório de Processos - CME")

    y = 750
    for processo in processos:
        p.drawString(50, y, f"Material: {processo.material.nome} - Serial: {processo.material.serial}")
        p.drawString(50, y - 20, f"Etapa: {processo.etapa} - Usuário: {processo.usuario.nome if processo.usuario else 'N/A'}")
        p.drawString(50, y - 40, f"Data Início: {processo.data_inicio} - Data Fim: {processo.data_fim}")
        y -= 60

        if y < 50:
            p.showPage()
            y = 800

    p.save()
    return response


#xlsx
def gerar_relatorio_xlsx(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório CME"

    ws.append(["Material", "Serial", "Etapa", "Usuário", "Data Início", "Data Fim"])

    processos = Processo.objects.all().order_by("material", "data_inicio")
    for processo in processos:
        ws.append([
            processo.material.nome,
            processo.material.serial,
            processo.etapa,
            processo.usuario.nome if processo.usuario else "N/A",
            processo.data_inicio,
            processo.data_fim
        ])

    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename="relatorio.xlsx"'
    wb.save(response)
    return response


def rastreabilidade(request):
    serial = request.GET.get('serial')
    processos = Processo.rastreabilidade(serial=serial)
    data = [
        {
            "material": processo.material.nome,
            "serial": processo.material.serial,
            "etapa": processo.etapa,
            "data_inicio": processo.data_inicio,
            "data_fim": processo.data_fim,
            "usuario": processo.usuario.nome if processo.usuario else None,
            "observacoes": processo.observacoes,
        }
        for processo in processos
    ]
    return render(request, 'rastreabilidade.html')


