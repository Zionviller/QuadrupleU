from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.uwu_fashion.urls')),
    url(r'^login/', include('apps.login_reg.urls')),
    url('', include('social_django.urls', namespace='social'))
]
