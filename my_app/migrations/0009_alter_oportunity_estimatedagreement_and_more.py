# Generated by Django 5.0.6 on 2024-07-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_oportunity_mustwin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunity',
            name='estimatedagreement',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='expenseprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='extrascope',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='materialprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='potentialprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='serviceprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='softwareprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='taxes',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='oportunity',
            name='totalprice',
            field=models.FloatField(null=True),
        ),
    ]
