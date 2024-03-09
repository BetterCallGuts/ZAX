from django.urls import path
from . import views


urlpatterns = [
  
    path("", views.check_product, name="check_product"),
    path("post-product/", views.manf_product_submit, name="post_product")
]
