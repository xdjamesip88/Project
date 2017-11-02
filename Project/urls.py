"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

# from LanCenter.views import Inicio, stockCreate, stockUpdate, stockList, stockDelete
from LanCenter.views import Inicio, cuentaList, cuentaDetail, cuentaCreation, cuentaUpdate, cuentaDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Inicio.as_view(), name='inicio'),


    url(r'^cuentaList', cuentaList.as_view(), name='cuentalist'),
    url(r'^cuentaDetail/(?P<pk>\d+)$', cuentaDetail.as_view(), name='cuentadetail'),
    url(r'^cuentaCreate', cuentaCreation.as_view(), name='cuentacreate'),
    url(r'^cuentaEdit/(?P<pk>\d+)$', cuentaUpdate.as_view(), name='cuentaedit'),
    url(r'^cuentaDelete/(?P<pk>\d+)$', cuentaDelete.as_view(), name='cuentadelete'),
    # url(r'^CrearStock/$', stockCreate.as_view(), name='createstock'),
    # url(r'^EditarStock/(?P<pk>\d+)$', stockUpdate.as_view(), name='editstock'),
    # url(r'^borrarStock/(?P<pk>\d+)$', stockDelete.as_view(), name='deletestock'),
    #


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
