
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from roadsafe_app.views import home,about,contact,service,eld,logistics,guide,test,test2,readmore
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('service/', service),
    path('eld/', eld),
    path('logistics/', logistics),
    path('guide/', guide),
    path('test/', test),
    path('test2/', test2),
    path('readmore/', readmore),
    


    
] + static(settings.MEDIA_URL,document_root=set)
