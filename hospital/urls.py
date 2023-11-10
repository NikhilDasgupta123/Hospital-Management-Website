from django.urls import path,include
from . import views
from .views import UserViewSet,DoctorViewSet,PatientViewSet,StaffViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Doctor', DoctorViewSet)
router.register(r'Patient', PatientViewSet)
router.register(r'Staff', StaffViewSet)


urlpatterns = [
    path('',views.home, name='home'),
    path('doctor_login',views.doctor_login,name='doctor_login'),
    path('logout',views.logout,name='logout'),
    path('patient_register',views.patient_register,name='patient_register'),
    path('doctor_after_login',views.doctor_after_login,name='doctor_after_login'),
    path('appointment_booking',views.appointment_booking,name='appointment_booking'),
    path('staff_admin',views.staff_admin,name='staff_page'),
    path('api', include(router.urls)),
]