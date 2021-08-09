
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('hello/',views.HelloAPIView.as_view()),
    path('customers/',views.CustomersView.as_view()),
    #path('customers/',views.CustomersView.as_view())
]
