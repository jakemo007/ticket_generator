from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('newticket',views.NewTicket.as_view(),name = 'new_ticket'),
    path('ticket/<int:pk>',views.TicketDetailView.as_view(),name='ticket_details'),
    path('article/edit/<int:pk>',views.EditTicketView.as_view(),name = 'edit_ticket'),
    path('article/delete/<int:pk>',views.DeleteTicketView.as_view(),name = 'delete_ticket'),
    path("logout", views.logout_request, name="logout")
]


