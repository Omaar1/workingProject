
from django.contrib import admin
from django.conf.urls import include,url
# from accounts.models import LoginForm

from products.views import  search , product_list_view

### changed !!!
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
#### --- >>
## logout -->
from django.contrib.auth.views import logout
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # url(r'^products-fbv/$', product_LView ),
    url(r'^(?P<category_id>[0-9]+)/$', views.cat, name="cat"),
    url(r'^category/(?P<course_id>[0-9]+)/$' , views.course_details, name="course_details"),
    url(r'^login$', views.login_page, name="login"),
    url(r'^register$', views.register_page , name="register"),
    ## new !!!!!
    url(r'^$', home_page, name="home_page"),
    url(r'^results/$', search , name ="search"),
    url(r'^join/(?P<course_id>[0-9]+)/$', join_course, name="join"),
    url(r'^profile$', profile, name="profile"),
    url(r'^payment/(?P<course_id>[0-9]+)/$', payment, name="payment"),
    url(r'^logout/$', logout, {'next_page': home_page }, name='logout'),
    url(r'^upload/$', views.upload, name="upload"),



    ###---->
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT , name="media")


""" url(r'^$', views.index, name="index")
 url('^products/',include('products.urls')) """
