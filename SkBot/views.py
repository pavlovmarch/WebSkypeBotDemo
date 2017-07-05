import os

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from django.views.static import serve

from SkBot import main_functions, hist



def index(request):
    if(hist.first == True):
        hist.first = False


    if(request.GET.get("start")):
        hist.history += "Получен список контактов\n"
        return render(request, 'templates\\SkBot\\contacts_pokazat.html', {"message": main_functions.allContacts(), "message2": main_functions.grayContacts(), "history": hist.history, "name": hist.name})

    return render(request, 'templates\\SkBot\\contacts_pokazat.html', {"history": hist.history, "name": hist.name})


def contacts_avtorizacia(request):
        if (request.GET.get("start")):
            main_functions.sendGrays(request.GET.get("msg"))
            hist.history += "Авторизация контактов\n"
            #hist.history += "test2\n"

        return render(request, 'templates\\SkBot\\contacts_avtorizacia.html', {"users": main_functions.grayContacts(), "history": hist.history, "name": hist.name })


def contacts_dobavlenie(request):
    if (request.GET.get("start")):
        main_functions.sendGreeting(request.GET.get("conts"), request.GET.get("msg"))
        hist.history = "Добавление контактов\n"
        #return render(request, 'templates\\SkBot\\contacts_dobavlenie.html', {"result": main_functions.sendGreeting(request.GET.get("conts"))})

    return render(request, 'templates\\SkBot\\contacts_dobavlenie.html', {"history": hist.history, "name": hist.name})


def contacts_chistka(request):
    if (request.GET.get("start")):
        hist.history = "Чистка контактов произведена\n"
        return render(request, 'templates\\SkBot\\contacts_chistka.html', { "result": main_functions.clear(), "history": hist.history, "name": hist.name})
    return render(request, 'templates\\SkBot\\contacts_chistka.html', {"name": hist.name})


def chatu_contactu(request):
    if(request.GET.get("start")):
        hist.history = "Получен список контактов чатов\n"
        return render(request, 'templates\\SkBot\\chatu_contactu.html', {"message3": main_functions.contactsFromChats(), "history": hist.history, "name": hist.name})
        #return HttpResponse(main_functions.contactsFromChats())
    return render(request, 'templates\\SkBot\\chatu_contactu.html', {"history": hist.history, "name": hist.name})


def chatu_rassulka(request):
    if (request.GET.get("mess_text")):
        hist.history += "Рассылка по чатам произведена\n"
        main_functions.sendChats(request.GET.get("mess_text"))
    return render(request, 'templates\\SkBot\\chatu_rassulka.html', {"history": hist.history, "name": hist.name})


def multiacc(request):
    if (request.GET.get("start")):
        hist.name = request.GET.get("login")
        hist.pwd = request.GET.get("pass")

    return render(request, 'templates\\SkBot\\multiacc.html', {"history": hist.history, "name": hist.name})


def parser_vk_po_grupam(request):
    return render(request, 'templates\\SkBot\\parser_vk_po_grupam.html', {"history": hist.history, "name": hist.name})


def parser_vk_po_liudiam(request):

    if (request.GET.get("start")):
        hist.history += "Парсинг по людям\n"
        main_functions.outputvk(request.GET.get("vk-login"), request.GET.get("vk-pass"))

    return render(request, 'templates\\SkBot\\parser_vk_po_liudiam.html', {"history": hist.history, "name": hist.name})



def rassulka_rassulka(request):
    if (request.GET.get("start")):
        hist.history += "Рассылка по пользователям произведена\n"
        main_functions.sendMsg(request.GET.get("message"))

    return render(request, 'templates\\SkBot\\rassulka_rassulka.html', {"history": hist.history, "name": hist.name})


def redactor_obiedenit_file(request):
    return render(request, 'templates\\SkBot\\redactor_obiedenit_file.html', {"history": hist.history, "name": hist.name})


def redactor_razbit_file(request):
    #if(request.GET.get(""))
    return render(request, 'templates\\SkBot\\redactor_razbit_file.html', {"history": hist.history, "name": hist.name})


def redactor_udalit_povtoru(request):
    return render(request, 'templates\\SkBot\\redactor_udalit_povtoru.html', {"history": hist.history, "name": hist.name})


def vugryzka(request):
    if (request.GET.get("start")):
        hist.history += "Рассылка по пользователям произведена\n"
        main_functions.output(request)
    return render(request, 'templates\\SkBot\\vugryzka.html', {"history": hist.history, "name": hist.name})



