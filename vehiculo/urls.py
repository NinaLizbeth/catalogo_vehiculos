from django.urls import path
from .views import index
from .views import vehiculos_list, add_vehiculos, signup , CustomLoginView, ver_vehiculo, eliminar_vehiculo, editar_vehiculo
from django.contrib.auth import views as auth_views
from .views import signup
from .views import RegisterView  # Importa la vista




urlpatterns = [
    path('', index, name='index'),  # '' hace que la vista index sea la vista principal

    path('vehiculos/', vehiculos_list, name='vehiculos_list'),

    path('fadd_vehiculos/', add_vehiculos, name='add_vehiculos'),
    
    path('accounts/login/', CustomLoginView.as_view(), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('accounts/signup/', signup, name='signup'), 

    path('vehiculo/<int:pk>/', ver_vehiculo, name='ver_vehiculo'),

    path('vehiculo/<int:pk>/editar/', editar_vehiculo, name='editar_vehiculo'),

    path('vehiculo/<int:pk>/eliminar/', eliminar_vehiculo, name='eliminar_vehiculo'), 

    path('register/', RegisterView.as_view(), name='register'),
]
