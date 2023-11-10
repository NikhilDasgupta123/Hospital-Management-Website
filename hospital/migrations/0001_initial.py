# Generated by Django 3.0.5 on 2022-06-07 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hospital.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True, unique=True)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Orthopedics', 'Orthopedics'), ('Physiotherapist', 'Physiotherapist'), ('Gynecologist', 'Gynecologist'), ('Neurologist', 'Neurologist'), ('Pediatrist', 'Pediatrist'), ('Urologist', 'Urologist')], max_length=40)),
                ('password', models.CharField(max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20, null=True, unique=True)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('staff_type', models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Ward Boy', 'Ward Boy'), ('Receptionist', 'Receptionist')], max_length=20, null=True)),
                ('password', models.CharField(max_length=16, null=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('department', models.CharField(blank=True, choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Orthopedics', 'Orthopedics'), ('Physiotherapist', 'Physiotherapist'), ('Gynecologist', 'Gynecologist'), ('Neurologist', 'Neurologist'), ('Pediatrist', 'Pediatrist'), ('Urologist', 'Urologist')], max_length=40, null=True)),
                ('password', models.CharField(max_length=256, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('symptoms', models.CharField(max_length=200, null=True)),
                ('disease', models.CharField(max_length=200, null=True)),
                ('admitdate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('file', models.FileField(upload_to=hospital.models.user_directory_path)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('symptoms', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('doctor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor')),
            ],
        ),
    ]