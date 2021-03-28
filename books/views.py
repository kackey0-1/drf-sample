from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.all()


@login_required
def library(request):
    output = f"""
        <html>
            <body>
                <h2>Library</h2>
                <p>{request.user.username}</p>
                <a href="/books/books/">Book API</a>
                <br/>
                <a href="/accounts/logout/">Logout</a>
            </body>
        </html>
    """
    return HttpResponse(output)


