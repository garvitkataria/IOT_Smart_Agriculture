"""IOT_Smart_Agriculture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
    path('userauth/', include('AuthUser.urls')),
	path('farm/', include('Farm.urls')),
	path('crop/', include('Crop_Type.urls')),
	path('sensor/', include('Sensors.urls')),
	path('items/', include('Items.urls')),
	path('transaction/', include('Transaction.urls')),
	url(r'^docs/', include_docs_urls(title='IOT Smart Agriculture'))
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)