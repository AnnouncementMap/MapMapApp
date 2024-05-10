from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test_response(request):
    return Response({'latitude':39.7738850, 'longitude':-086.1761408, 'attributes':{'title':'IUPUI', 'tag':'Event'}})


