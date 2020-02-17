"""cs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_swagger_view(title='API Dorian')

schema_view2 = get_schema_view(
   openapi.Info(
      title="API Dorian",
      default_version='v1',
      description="Swagger 2",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="173258@ids.upchiapas.edu.mx"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^api/v1/', include('Login.urls')),
    re_path(r'^api/v2/', include('Profile.urls')),

    url(r'api/', schema_view),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view2.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view2.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view2.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]