# Generated by Django 3.2.7 on 2021-09-13 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210913_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='dataset_brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='api.dataset'),
        ),
        migrations.AlterField(
            model_name='link',
            name='dataset_link',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='api.dataset'),
        ),
        migrations.AlterField(
            model_name='source',
            name='dataset_source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='api.dataset'),
        ),
    ]
