from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import get_dashboard_statistics
from .serializers import DashboardSerializer


class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        data = get_dashboard_statistics()

        serializer = DashboardSerializer(data)

        return Response(serializer.data)