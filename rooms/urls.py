from django.urls import path,include
from .filters import roomSearch

from . import views

urlpatterns = [
    path("room-list/", views.RoomList.as_view()),
    path("room-details/", views.RoomDetails.as_view()),
    path("create-department-room/", views.createRoom, name="create-department-room"),
    path("get-department-rooms/", views.getDepartmentRooms, name="get-department-rooms"),
    path("update-department-room/", views.updateDepartmentRoom, name="update-department-room"),
    path("rooms-search/", roomSearch, name="rooms_search"),
    path("export-rooms-pdf/", views.generate_rooms_pdf, name="export-rooms-pdf"),
    path("export-rooms-excel/", views.generate_rooms_excel, name="export-rooms-excel"),
    path("export-rooms-csv/", views.generate_rooms_csv, name="export-rooms-csv"),
    path("display-rooms-import-excel/", views.display_rooms_import_excel, name="display-rooms-import-excel"),
    path("import-rooms-excel/", views.import_rooms_excel, name="import-rooms-excel"),
    path("delete-room/", views.deleteRoom, name="delete-room"),
]
