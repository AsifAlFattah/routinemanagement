# Generated by Django 5.0.2 on 2024-05-14 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_studentinfo_diploma_intake_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Allocation_to_Diploma_Intake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomallocations', to='core.allocatedroom')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomallocations', to='core.studentinfo_diploma_intake')),
            ],
        ),
    ]
