from django.db import migrations

def delete_existing_curriculam(apps, schema_editor):
    Curriculam = apps.get_model('core', 'Curriculam')
    Curriculam.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_curriculam_semester'),
    ]

    operations = [
        migrations.RunPython(delete_existing_curriculam),
    ]
