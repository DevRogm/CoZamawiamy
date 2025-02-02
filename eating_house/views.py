from django.db import transaction
from django.db.models import ProtectedError
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from eating_house.models import EatingHouse
from eating_house.serializers import EatingHouseSerializer


class CreateEatingHouseAPIView(CreateAPIView):
    queryset = EatingHouse.objects.all()
    serializer_class = EatingHouseSerializer
    permission_classes = [IsAdminUser]


class EditEatingHouseAPIView(UpdateAPIView):
    queryset = EatingHouse.objects.all()
    serializer_class = EatingHouseSerializer
    permission_classes = [IsAdminUser]


class DetailsEatingHouseAPIView(RetrieveAPIView):
    queryset = EatingHouse.objects.all()
    serializer_class = EatingHouseSerializer
    permission_classes = [IsAdminUser]


class DeleteEatingHouseAPIView(DestroyAPIView):
    queryset = EatingHouse.objects.all()
    serializer_class = EatingHouseSerializer
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            with transaction.atomic():
                if instance.address:
                    instance.address.delete()
                instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(
                {"error": "Nie można usunąć adresu, ponieważ jest chroniony przez EatingHouse."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListEatingHouseAPIView(ListAPIView):
    queryset = EatingHouse.objects.all()
    serializer_class = EatingHouseSerializer
    permission_classes = [IsAdminUser]
