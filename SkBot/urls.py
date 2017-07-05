from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', 'SkBot.views.index', name='index'),
    url(r'chatu_contactu', 'SkBot.views.chatu_contactu', name='chatu_contactu'),
    url(r'chatu_rassulka', 'SkBot.views.chatu_rassulka', name='chatu_rassulka'),
    url(r'contacts_avtorizacia', 'SkBot.views.contacts_avtorizacia', name='contacts_avtorizacia'),
    url(r'contacts_chistka', 'SkBot.views.contacts_chistka', name='contacts_chistka'),
    url(r'contacts_dobavlenie', 'SkBot.views.contacts_dobavlenie', name='contacts_dobavlenie'),
    url(r'multiacc', 'SkBot.views.multiacc', name='multiacc'),
    url(r'parser_vk_po_grupam', 'SkBot.views.parser_vk_po_grupam', name='parser_vk_po_grupam'),
    url(r'parser_vk_po_liudiam', 'SkBot.views.parser_vk_po_liudiam', name='parser_vk_po_liudiam'),
    url(r'rassulka_rassulka', 'SkBot.views.rassulka_rassulka', name='rassulka_rassulka'),
    url(r'redactor_obiedenit_file', 'SkBot.views.redactor_obiedenit_file', name='redactor_obiedenit_file'),
    url(r'redactor_razbit_file', 'SkBot.views.redactor_razbit_file', name='redactor_razbit_file'),
    url(r'redactor_udalit_povtoru', 'SkBot.views.redactor_udalit_povtoru', name='redactor_udalit_povtoru'),
    url(r'vugryzka', 'SkBot.views.vugryzka', name='vugryzka'),
]