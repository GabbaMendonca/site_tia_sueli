from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.http import Http404
from django.core.mail import send_mail

def index(request):
    return render(request, 'website/index.html')

def contato(request):
    return render(request, 'website/contato.html')

def enviar(request):
    if request.method != 'POST':
        raise Http404()

    nome = request.POST.get('nome', None)
    mensagem = request.POST.get('mensagem', None)
    email = request.POST.get('email', None)

    if not nome or not email or not mensagem:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'website/fale_comigo.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'website/fale_comigo.html')
    else:

        try:
            send_mail(

                #Assunto:
                "E-mail do Site",
                #Mensagem:
                "Oi, eu sou " + nome + "\n" + mensagem,
                #Endereço do remetente:
                email,
                #Email para onde enviar
                ['admin@example.com']

            )
        except:
            messages.error(request, 'Ocorreu um erro durante o envio da mensagem.')
            return render(request, 'website/fale_comigo.html')
        else:
            messages.success(request, 'Mensagem enviada com sucesso !')



    return redirect('index')
