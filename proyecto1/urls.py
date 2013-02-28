from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from books import views
urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    (r'^search-form/$', views.busqueda_form),
    (r'^busqueda/$', views.search),

)
