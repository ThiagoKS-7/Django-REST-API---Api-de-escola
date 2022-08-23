# Generated by Django 4.1 on 2022-08-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
                ("rg", models.CharField(max_length=10)),
                ("cpf", models.CharField(max_length=15)),
                ("idade", models.IntegerField()),
                ("dt_nasc", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
