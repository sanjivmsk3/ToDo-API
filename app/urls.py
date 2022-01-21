from django.urls import path
from . import views
  
urlpatterns = [
      path('all/', views.all_details, name="all"),    # For view all items
      path('create/', views.create_detail, name="create"),  # For Create Item
      path('update/<int:pk>', views.update_detail, name="update"),      # For update Item
      path('delete/<int:pk>', views.delete_detail, name="delete"),      # For delete Item
]