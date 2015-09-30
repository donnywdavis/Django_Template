from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'static_pages.views.index', name='home'),
]
