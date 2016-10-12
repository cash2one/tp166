"""ty166 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from rest_framework import routers, serializers, viewsets
from cms.models import Content

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ('id','title', 'isMedia', 'content', 'created_date')

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ArticleSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)

urlpatterns = [
                  url(r'^api/', include(router.urls)),
                  url(r'^admin/', admin.site.urls),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),

                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
                  # REST APT
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^account/', include('account.urls',namespace='account')),
                  url(r'^cms/', include('cms.urls',namespace='cms')),


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
