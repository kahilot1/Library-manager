# Generated by Django 4.1.3 on 2022-11-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0002_alter_books_book_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="book_owner",
            field=models.CharField(max_length=100),
        ),
    ]
