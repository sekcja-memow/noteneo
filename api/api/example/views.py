from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloViewSet(ViewSet):
    """
    Hello world api endpoint without auth
    """
    permission_classes = []

    def list(self, request):
        return Response({"message": "Hello, world"})


class AuthHelloViewSet(ViewSet):
    """
    Hello world api endpoint with auth
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({"message": "Hello, world"})
