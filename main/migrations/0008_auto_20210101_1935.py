# Generated by Django 3.1.4 on 2021-01-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_schemascolumn_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemascolumn',
            name='category',
            field=models.CharField(choices=[('full_name', 'Full name'), ('email', 'Email'), ('phone_number', 'Phone number'), ('integer', 'Integer'), ('text', 'Text')], default='full_name', max_length=12),
        ),
    ]
