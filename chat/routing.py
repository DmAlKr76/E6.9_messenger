from django.urls import re_path, path
from chat.consumers import RoomConsumer, DirectConsumer

# websocket_urlpatterns = [
#   re_path(r'^ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi())
#   re_path(r'^ws/chat/direct/(?P<direct_name>\w+)/$', DirectConsumer.as_asgi())
# ]

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', RoomConsumer.as_asgi()),
    path('ws/chat/direct/<str:direct_name>/', DirectConsumer.as_asgi())
]
