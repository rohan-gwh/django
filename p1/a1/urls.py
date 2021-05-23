from django.conf.urls import url
from a1 import views
from django.urls import path,re_path



app_name =  'a1'

urlpatterns= [
    re_path(r'^register/$',views.register,name='register'),
    #re_path(r'^other/$',views.other,name='other'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),

]
