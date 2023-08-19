from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'Grocery_app'  # Namespace for the app's URLs

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),  # List view
    path('create/', ProductCreateView.as_view(), name='product-create'),  # Create view
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),  # Update view
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),  # Delete view
]