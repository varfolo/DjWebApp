"""
Definition of urls for DjWebApp.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static


import store.views
import store.forms



import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', store.views.index, name='home'),
    url(r'^registration', store.views.registration, name='registration'),
    url(r'^account/(?P<user_id>\d+)/$',store.views.account, name = 'account'),
    url(r'^logout$', store.views.log_out, name='logout'),
    url(r'^error$', store.views.error, name='error'),
    url(r'^log_in$', store.views.log_in, name='log_in'),
    #url(r'^login$', store.views.Login, name='login'),
    url(r'^add$', store.views.add, name = 'add'),
    url(r'^item/(?P<prod_id>[0-9]+)/$',store.views.item, name = 'detail'),
    #url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
   # url(r'^login/$',
   #     django.contrib.auth.views.login,
   #     {
   #         'template_name': 'app/login.html',
   #         'authentication_form': app.forms.BootstrapAuthenticationForm,
   #         'extra_context':
   #         {
   #             'title': 'Log in',
   #             'year': datetime.now().year,
   #         }
   #     },
   #     name='login'),
   # url(r'^logout$',
   #     django.contrib.auth.views.logout,
   #     {
   #         'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin: 
    # url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
