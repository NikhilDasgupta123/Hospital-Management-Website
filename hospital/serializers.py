from rest_framework import serializers
from .models import User,Doctor,Patient,Staff

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class DoctorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class StaffSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"