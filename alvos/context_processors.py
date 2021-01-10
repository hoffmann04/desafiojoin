from .models import Alvo

# Disponibiliza todos os alvos no contexto
def todos_alvos(request):
    todos_alvos = Alvo.objects.all()

    return {'alvos': todos_alvos}