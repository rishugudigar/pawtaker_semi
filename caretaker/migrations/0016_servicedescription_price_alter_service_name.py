# Generated by Django 4.2 on 2023-06-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0015_remove_service_price_remove_servicedescription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedescription',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(choices=[('Pet Boarding', 'Pet Boarding'), ('Pet Grooming', 'Pet Grooming')], max_length=100),
        ),
    ]
