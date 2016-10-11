from django.conf.urls import url, include

urlpatterns = [
    # post views
    url('^', include('django.contrib.auth.urls')),
]
