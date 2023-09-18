from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),
  # path('login/', auth_views.LoginView.as_view(), name='login'),
  # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('index/', views.student_search, name='student_search'),
  path('export_excel/', views.export_to_excel, name='export_to_excel'),
  path('import_excel/', views.import_from_excel, name='import_from_excel'),
]
