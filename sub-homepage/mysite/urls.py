from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite import views

app_name = 'mysite'

urlpatterns = [
    path('', views.base1, name='base1'), 
    path('blog/new_post/', views.new_post, name="new_post"),
    path('blog/food_list/', views.food_list, name="food_list"),
    path('blog/food_list1/', views.food_list1, name="food_list1"),
    path('blog/map/', views.map, name='map'),
    path('blog/base1/', views.base1, name='base1'),  
    path('blog/molar/', views.molar, name='molar'),
    path('blog/blog1/', views.blog1, name='blog1'),
    
    #메뉴
    path('blog/map/', views.map, name='map'),
    path('blog/map/gotowork', views.gotowork, name='gotowork'),
    path('blog/map/gotowork', views.gunae, name='gunae'),
    path('blog/map/rol', views.rol, name='rol'),
    path('blog/map/dol', views.dol, name='dol'),
    path('blog/map/lee', views.lee, name='lee'),
    path('blog/map/mak', views.mak, name='mak'),
    path('blog/map/mij', views.mij, name='mij'),
    path('blog/map/bac1', views.bac1, name='bac1'),
    path('blog/map/bac2', views.bac2, name='bac2'),
    path('blog/map/bac3', views.bac3, name='bac3'),
    path('blog/map/bon', views.bon, name='bon'),
    path('blog/map/bun', views.bun, name='bun'),
    path('blog/map/bac4', views.bac4, name='bac4'),
    path('blog/map/bac5', views.bac5, name='bac5'),
    path('blog/map/sae', views.sae, name='sae'),
    path('blog/map/sun', views.sun, name='sun'),
    path('blog/map/yuk', views.yuk, name='yuk'),
    path('blog/map/yeo', views.yeo, name='yeo'),
    path('blog/map/one', views.one, name='one'),
    path('blog/map/ins', views.ins, name='ins'),
    path('blog/map/jes', views.jes, name='jes'),
    path('blog/map/han', views.han, name='han'),
    path('blog/map/hon', views.hon, name='hon'),
    
    path('blog/sfood', views.show_food, name='food'),
    path('blog/show_post', views.show_post, name='show'),
    path('blog/fchoice/', views.fchoice, name='flist'),
    path('blog/foodview/', views.foodview, name='finale'),

    # path('blog/predict/', views.predict_model, name='predict_model'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)