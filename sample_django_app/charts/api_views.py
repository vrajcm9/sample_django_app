from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def chart_data_api(request):
    # Sample data
    data = {"x": [0, 1, 2, 3, 4, 5], "y": [3, 12, 5, 18, 45, 8]}
    return Response(data)
