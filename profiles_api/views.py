from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API view """
    def get(self, request, format=None):
        """Returns a list of APIVies features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            ''
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})