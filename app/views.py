from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def resena_historica(request):
    return render(request, 'facultad/resena_historica.html')

def mision_vision(request):
    return render(request, 'facultad/mision_vision.html')

def transparencias(request):
    return render(request, 'facultad/transparencias.html')

def reglamentos(request):
    return render(request, 'facultad/reglamentos.html')

def autoridades(request):
    return render(request, 'facultad/autoridades.html')

def sistemas(request):
    return render(request, 'escuela/sistemas.html')

def transportes(request):
    return render(request, 'escuela/transportes.html')

def agroindustrial(request):
    return render(request, 'escuela/agroindustrial.html')

def industrial(request):
    return render(request, 'escuela/industrial.html')

def gestion_academica(request):
    return render(request, 'estudiantes/gestion_academica.html')

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

def biblioteca(request):
    return render(request, 'investigacion/biblioteca.html')

def correo(request):
    return render(request, 'estudiantes/correo.html')

def calendario(request):
    return render(request, 'estudiantes/calendario.html')

def trabajo(request):
    return render(request, 'estudiantes/trabajo.html')

def tramite(request):
    return render(request, 'estudiantes/tramite.html')

def gestion_academica(request):
    return render(request, 'estudiantes/gestion_academica.html')    

def gestion_administrativa(request):
    return render(request, 'estudiantes/gestion_administrativa.html')

def segunda_especialidad(request):
    return render(request, 'estudiantes/segunda_especialidad.html')

def tupa(request):
    return render(request, 'estudiantes/tupa.html')

def oficinas(request):
    return render(request, 'oficinas/oficinas.html')

def nacionales(request):
    return render(request, 'convenios/nacionales.html')

def internacionales(request):
    return render(request, 'convenios/internacionales.html')

def interinstitucionales(request):
    return render(request, 'convenios/interinstitucionales.html')

