from django.urls import path
from web.views import index, subscribe, contact,product



app_name = "web"


urlpatterns = [
    path('',index, name="index"),
    path('subscribe/',subscribe, name="subscribe"),
    path('contact/',contact, name="contact"),
    #  veriable an '<int:pk>' == id an <int:> -> koduthal safe an(error anangil 404 il nilkkum)
    path('product/<int:pk>',product, name="product",),


    


]