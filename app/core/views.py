import os
from base64 import b64decode
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Message, MessagePart
from core.utils import read_json, MESES, localdate


def index(request):
    contas = Message.objects.raw('SELECT 0 id, `to` FROM core_message GROUP BY `to`')
    for conta in contas:
        print(conta.__dict__)

    messages = Message.objects.filter(deleted=False).order_by('-created_at')

    for message in messages:
        data = localdate(message.created_at)
        message.parts = MessagePart.objects.filter(message=message)

        try:
            message.resumo = message.parts[0].content[:256].replace('\n', ' ')
        except:
            print('ERRO: não foi possível obter resumo')
            message.resumo = ''

        message.data = MESES[data.month] + f' {data.day}'
        message.data_full = data.strftime('%d/%m/%Y - %H:%M')

    return render(request, 'index.html', {
        'messages': messages,
    })


@csrf_exempt
def login(request):
    senha = os.environ.get('CARTEIRO_SENHA')

    if request.POST:
        pw = request.POST['senha']

        if senha and pw == senha:
            request.session['user'] = True
            return redirect('/')
    
    return render(request, 'login.html', {
    })


def logout(request):
    request.session.flush()
    return redirect('/login')


@csrf_exempt
def read(request):
    if request.POST:
        pk = int(request.POST['id'])
        message = Message.objects.get(pk=pk)
        message.read = True
        message.save()
    return HttpResponse()


@csrf_exempt
def delete(request):
    if request.POST:
        pk = int(request.POST['id'])
        MessagePart.objects.filter(message__id=pk).delete()
        message = Message.objects.get(pk=pk)
        message.delete()
        #message.deleted = True
        #message.save()
    return HttpResponse()


@csrf_exempt
def hook(request):
    data = read_json(request)

    if data:
        message = Message(
            from_email=data['from_email'],
            from_name=data['from_name'],
            to=data['to'],
            subject=data['subject'],
        )
        message.save()

        for part in data['parts']:
            mp = MessagePart(
                message=message,
                content_type=part[0],
                content=b64decode(part[1]).decode(),
            )
            mp.save()

    return HttpResponse()
