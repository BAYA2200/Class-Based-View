from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Product, Firm, Category
from shop.serializers import ProductSerializer, FirmSerializer, CategorySerializer

# проверил через postman, работает нормально

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# проверил через postman, работает нормально

class FirmListCreateAPIView(ListCreateAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class FirmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

# проверил через postman, работает нормально
class CategoryAPIView(APIView):
    def get(self, request):
        p = Category.objects.all()
        serializers = CategorySerializer(p, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        snippet = Category.objects.get(pk=pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = Category.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

