from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def resena_historica(request):
    return render(request, 'facultad/resena_historica.html')

def mision_vision(request):
    return render(request, 'facultad/mision_vision.html')

def transparencias(request):
    documentos = [
        {"titulo": "Estatuto de la Universidad", "enlace": "/ruta/estatuto.pdf"},
        {"titulo": "Reglamento General", "enlace": "/ruta/reglamento.pdf"},
        {"titulo": "Decretos Supremos", "enlace": "/ruta/decretos.pdf"},
        {"titulo": "Plan Estratégico Institucional", "enlace": "/ruta/plan.pdf"},
        {"titulo": "Información del Presupuesto Institucional", "enlace": "/ruta/presupuesto.pdf"},
        {"titulo": "Información Académica", "enlace": "/ruta/academica.pdf"},
        {"titulo": "Información Docente", "enlace": "/ruta/docente.pdf"},
    ]
    return render(request, 'facultad/transparencias.html', {'documentos': documentos})

def resoluciones_actas_reglamentos(request):
    return render(request, 'facultad/resoluciones_actas_reglamentos.html')

def autoridades(request):
    return render(request, 'facultad/autoridades.html')

def programacion(request):
    return render(request, 'capacitacion/programacion.html')

def gestion(request):
    return render(request, 'capacitacion/gestion.html')

def ciberseguridad(request):
    return render(request, 'capacitacion/ciberseguridad.html')

def bigdata(request):
    return render(request, 'capacitacion/bigdata.html')

def eventos(request):
    return render(request, 'eventos/eventos.html')