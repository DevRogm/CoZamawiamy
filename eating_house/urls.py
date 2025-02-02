from django.urls import path

from eating_house.views import CreateEatingHouseAPIView, EditEatingHouseAPIView, DetailsEatingHouseAPIView, \
    DeleteEatingHouseAPIView, ListEatingHouseAPIView

app_name = 'eating_house'

urlpatterns = [
    path('create/', CreateEatingHouseAPIView.as_view(), name='create_eating_house'),
    path('edit/<int:pk>/', EditEatingHouseAPIView.as_view(), name='edit_eating_house'),
    path('details/<int:pk>/', DetailsEatingHouseAPIView.as_view(), name='details_eating_house'),
    path('delete/<int:pk>/', DeleteEatingHouseAPIView.as_view(), name='delete_eating_house'),
    path('list/', ListEatingHouseAPIView.as_view(), name='list_eating_house'),
]
