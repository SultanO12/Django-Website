from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.exceptions import ValidationError
from main.models import Catigory, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from authentication.serializers import RegisterSerializer

class RegisterUserView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(data=serializer.data)


class CategoryViewSet(GenericAPIView):
    def list(self, request):
        queryset = Catigory.objects.all()
        serializer = CategorySerializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

# @permission_classes([IsAuthenticatedOrReadOnly])
class CategoryListGenericAPIView(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Catigory.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET', 'POST'])
def main(request: Request):
    if request.method == "POST":
       serializer = CategorySerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       cat = Catigory.objects.create(**serializer.validated_data)
       cat_sr = CategorySerializer(cat)
       return Response(data={"Create":cat_sr.data}, status=status.HTTP_201_CREATED)
    else:
        cats = Catigory.objects.all()
        serializer = CategorySerializer(instance=cats, many=True)
        return Response(data={"Categories":serializer.data}, status=status.HTTP_200_OK)

class CategoryRetrieveUpdateDestroyGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Catigory.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk):
        serializer = self.serializer_class(instance=self.get_object())
        return Response(data=serializer.data)

    def put(self, request, pk):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, pk):
        object = self.get_object()
        object.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
    
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'