from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.display, name='display'),
    url(r'^register', views.registration, name='registration'),
    url(r'^login', views.login, name='login'),
    url(r'^detail', views.DetailView.as_view(), name='login'),

]
