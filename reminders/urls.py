from django.urls import path
from .views import ReminderCreateView, ReminderListView, ReminderDetailView

urlpatterns = [
    path('create/', ReminderCreateView.as_view(), name='create-reminder'),
    path('list/', ReminderListView.as_view(), name='list-reminders'),
    path('<int:pk>/', ReminderDetailView.as_view(), name='detail-reminder'),
]
