# Generated by Django 1.11.17 on 2019-03-20 10:25

from django.db import migrations


def remove_unusednewbase_alert(apps, schema_editor):
    Alert = apps.get_model("trans", "Alert")
    db_alias = schema_editor.connection.alias
    Alert.objects.using(db_alias).filter(name="UnusedNewBase").delete()


class Migration(migrations.Migration):

    dependencies = [("trans", "0017_component_language_code_style")]

    operations = [migrations.RunPython(remove_unusednewbase_alert, elidable=True)]
