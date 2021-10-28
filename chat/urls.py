from django.urls import path
from chat.views import * #index, chat_room, private_room, DetailUserViewAPI, GetCurrentUserViewAPI, GetPublicRoomsViewAPI, \
    #GetPublicRoomsOfUserViewAPI

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    path('direct/<str:direct_name>/', direct, name='direct'),
    #path('accounts/account_details/<str:username>/', account_details, name="account_details"),
    path('api/v1/accounts/detail/<str:username>/', UserAPIView.as_view(), name='user_api'),
    path('api/v1/accounts/get_author/', GetUserAPIView.as_view(), name='get_user_api'),
    path('api/v1/get_rooms/', GetRoomsAPIView.as_view(), name='get_rooms_api'),
    path('api/v1/get_rooms_of_author/<str:username>/', GetRoomsOfUserAPIView.as_view(), name='get_rooms_of_user'),
]
