from django.urls import path, include 
from . import views 


urlpatterns = [
    
    path('products/',views.Products ,name='products'),
    path('addproduct/',views.AddProduct ,name='addproduct'),
    path('deleteproduct/<int:id>/',views.DeleteProduct , name = 'deleteproduct' ),
    path('updateproduct/<int:id>/',views.UpdateProduct , name = 'updateproduct' ),
    path('category/',views.Categorry ,name='category'),
    path('brand/',views.Brandds ,name='brand'),
    path('deletecategory/<int:id>/',views.DeleteStatus ,name='deletecategory'),
    path('recovercategory/<int:id>/',views.RecoverStatus ,name='recovercategory'),
    path('deletebrand/<int:id>/',views.BrandSoftDelete ,name='deletebrand'),
    path('recoverbrand/<int:id>/',views.BrandSoftrecover ,name='recoverbrand'),
    

 ]