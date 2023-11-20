from store.serializer import BookSerializer
from rest_framework.viewsets import ModelViewSet
from store.models import Book
# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
