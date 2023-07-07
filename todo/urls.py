from django.urls import path
from .views import AllCreateTodoView,DetailUpdateDeleteApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path("",ListItems.as_view()),
    #path("<int:todomodel_id>",DetailTodo.as_view()),
    #path("create",CreateTodoView.as_view()),
    #path("update/<int:todomodel_id>",UpdateTodomodel.as_view()),
    #path("update_status/<int:todomodel_id>", UpdateStatus.as_view()),
    #path("delete/<int:todomodel_id>",DeleteTodomodel.as_view()),
    #path("status/<str:status>",GetStatusView.as_view()),
    path("",AllCreateTodoView.as_view()),
    path("<pk>",DetailUpdateDeleteApiView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]