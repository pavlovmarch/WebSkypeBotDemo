from django.conf.urls import include, url
from django.contrib import admin


import settings
from SkBot import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'WebSkypeBot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', include('SkBot.urls')),
    url(r'^chatu_contactu/', views.chatu_contactu, name="chatu_contactu"),
    #url(r'^chatu_contactu', include('SkBot.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vugryzka/', views.vugryzka, name="vugryzka"),
    url(r'^redactor_udalit_povtoru/', views.redactor_udalit_povtoru, name="redactor_udalit_povtoru"),
    url(r'^redactor_razbit_file/', views.redactor_razbit_file, name="redactor_razbit_file"),
    url(r'^redactor_obiedenit_file/', views.redactor_obiedenit_file, name="redactor_obiedenit_file"),
    url(r'^rassulka_rassulka/', views.rassulka_rassulka, name="rassulka_rassulka"),
    url(r'^parser_vk_po_liudiam/', views.parser_vk_po_liudiam, name="parser_vk_po_liudiam"),
    url(r'^parser_vk_po_grupam/', views.parser_vk_po_grupam, name="parser_vk_po_grupam"),
    url(r'^multiacc/', views.multiacc, name="multiacc"),
    url(r'^contacts_dobavlenie/', views.contacts_dobavlenie, name="contacts_dobavlenie"),
    url(r'^contacts_chistka/', views.contacts_chistka, name="contacts_chistka"),
    url(r'^contacts_avtorizacia/', views.contacts_avtorizacia, name="contacts_avtorizacia"),
    url(r'^chatu_rassulka/', views.chatu_rassulka, name="chatu_rassulka"),







]
