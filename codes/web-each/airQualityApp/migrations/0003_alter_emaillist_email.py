# Generated by Django 4.2.1 on 2023-07-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airQualityApp", "0002_alter_emaillist_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emaillist",
            name="email",
            field=models.EmailField(
                error_messages={
                    "unique:This email has already been registered. Please use a different email."
                },
                max_length=254,
                unique=True,
            ),
        ),
    ]
