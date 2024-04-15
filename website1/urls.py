from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'website1'

urlpatterns = [
	path('', views.home, name = 'home'),
    path('itdept', views.itdept, name='itdept'),
    path('compsdept', views.compsdept, name='compsdept'),
    path('mechdept', views.mechdept, name='mechdept'),
    path('extcdept', views.extcdept, name='extcdept'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('editdata', views.edit_data, name='editdata'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
