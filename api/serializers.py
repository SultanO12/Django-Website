import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from main.models import Product, Catigory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catigory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class PostModel:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=2000)

def encode():
    model = PostModel(title="Test title", content="Test content")
    model_sr = PostSerializer(instance=model)
    print(model_sr.data, type(model_sr.data), sep="\n")
    json = JSONRenderer().render(data=model_sr.data)
    print(json)

def decode():
    json = b'{"title":"Test title","content":"Test content"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream=stream)
    serializer = PostSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)