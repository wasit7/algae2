"""algae_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include

admin.site.site_header = 'Algae Admin'
admin.site.site_title = 'Algae Admin'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^algae/', include('algae_app.urls', namespace="algae") ),
    url(r'^$', views.water, name='home'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG is True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)