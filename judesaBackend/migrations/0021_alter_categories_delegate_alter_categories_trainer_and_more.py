# Generated by Django 5.1.1 on 2024-09-24 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judesaBackend', '0020_alter_categories_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='delegate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delegate_id', to='judesaBackend.staff'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_id', to='judesaBackend.staff'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_id_matches', to='judesaBackend.categories'),
        ),
        migrations.AlterField(
            model_name='players',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_id_players', to='judesaBackend.categories'),
        ),
    ]