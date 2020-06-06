"""cfehome URL Configuration

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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic.base import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="LRAQWorker Mockup API",
      default_version='v1',
      description="LRAQWorker Mockup API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', auth_views.LoginView.as_view()),
    url(r'^v1/authenticate$', obtain_jwt_token, name='api-login'),
    url(r'^v1/$', RedirectView.as_view(url='/', permanent=True), name='api-v1'),   
    url(r'^v1/controlmatrix/$', RedirectView.as_view(url='/', permanent=True), name='api-v1'),       
#    url(r'^v1/controlmatrix/surveycreated/', include(('postings.api.urls', 'api-lraqworker'), namespace='api-lraqworker')),
    url(r'^v1/controlmatrix/surveycreated/', include(('postings.api.urls', 'api-lraqworker'), namespace='api-lraqworker')),
    url(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

