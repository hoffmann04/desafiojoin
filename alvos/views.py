from django.shortcuts import render
from .models import Alvo
from .forms import AlvoForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return render(request, 'alvos/index.html', {})


# View para adicionar um alvo
def adicionar_alvo(request):
    # Se não por POST então envia o form para preencher
    # Se for POST, salva o novo alvo e carrega o index
    if request.method == 'POST':
        adicionar_alvo_form = AlvoForm(data=request.POST)
        if adicionar_alvo_form.is_valid():
            novo_alvo = adicionar_alvo_form.save(commit=False)
            novo_alvo.save()
            return redirect('alvos:index')
        else:
            messages.error(request, 'Preencha o Formulário')
    else:
        adicionar_alvo_form = AlvoForm()

    return render(request, 'alvos/criar_alvo.html', {'adicionar_alvo_form': adicionar_alvo_form})


# View para editar um alvo
def edit_alvos(request, alvo_id):
    # Procura o alvo que vai ser editado
    alvo = Alvo.objects.get(pk=alvo_id)

    # Se for POST, salva os novos dados do alvo
    # Senão, manda os dados do alvo atual para ser editado
    if request.method == 'POST':
        alvo_form = AlvoForm(instance=alvo, data=request.POST)
        if alvo_form.is_valid():
            alvo_form.save()
            return redirect('alvos:index')
        else:
            messages.error(request, 'Preencha o Formulário')
    else:
        alvo_form = AlvoForm(instance=alvo)

    # Manda o alvo.id no contexto pois é necessário caso o usuário queira deletar o alvo
    return render(request, 'alvos/editar_alvo.html', {'alvo_form': alvo_form, 'alvoid': alvo.id})


# View para deletar um alvo
def deletar_alvo(request, alvo_id):
    # Procura o alvo que vai ser deletado e então o deleta
    alvo = Alvo.objects.filter(pk=alvo_id)
    alvo.delete()

    return redirect('alvos:index')
