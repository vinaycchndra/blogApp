# Generated by Django 4.2 on 2023-06-08 14:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blogApi', '0002_alter_comments_options_comments_parent'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comments',
            managers=[
                ('nonParent', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApi.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=1000),
        ),
    ]
