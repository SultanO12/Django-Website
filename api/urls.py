from django.urls import path
from .views import main, ProductRetrieveUpdateDestroyAPIView, ProductListCreateAPIView, CategoryRetrieveUpdateDestroyGenericAPIView, CategoryListGenericAPIView, CategoryViewSet, RegisterUserView

urlpatterns = [
    path("cats/", CategoryListGenericAPIView.as_view(), name="main-api"),
    path("cat/<int:pk>/", CategoryRetrieveUpdateDestroyGenericAPIView.as_view(), name="catigory-api"),
    path("products/", ProductListCreateAPIView.as_view(), name="products-api"),
    path("product/<int:pk>/", ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-api"),
]