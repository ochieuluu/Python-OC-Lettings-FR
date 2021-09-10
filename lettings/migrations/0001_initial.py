# Generated by Django 3.0 on 2021-08-15 16:34

""" After code refactoring:
- Step 1:  let Django generate automatically migration files
- Step 2: Generated manually
+ Replace migrations.CreateModel(...) by migrations.SeparateDatabaseAndState()
+ Put migrations.CreateModel(...) in state_operations and in add database_operations=[]
"""


import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        ### Generated automatically

        # migrations.CreateModel(
        #     name='Address',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
        #         ('street', models.CharField(max_length=64)),
        #         ('city', models.CharField(max_length=64)),
        #         ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
        #         ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
        #         ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
        #     ],
        #     options={
        #         'verbose_name_plural': 'Addresses',
        #     },
        # ),

        ### Generated manually from lines above in putting migrations.CreateModel(...) in state_operations and adding database_operations=[]
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Address',
                    fields=[
                        ('id',
                         models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                          verbose_name='ID')),
                        ('number', models.PositiveIntegerField(
                            validators=[django.core.validators.MaxValueValidator(9999)])),
                        ('street', models.CharField(max_length=64)),
                        ('city', models.CharField(max_length=64)),
                        ('state', models.CharField(max_length=2, validators=[
                            django.core.validators.MinLengthValidator(2)])),
                        ('zip_code', models.PositiveIntegerField(
                            validators=[django.core.validators.MaxValueValidator(99999)])),
                        ('country_iso_code', models.CharField(max_length=3, validators=[
                            django.core.validators.MinLengthValidator(3)])),
                    ],
                    options={
                        'verbose_name_plural': 'Addresses',
                    },
                ),
            ],
            # Table already exists. See  oc_lettings_site/migrations/0003_auto_20210815_1634.py
            database_operations=[],
        ),

        # migrations.CreateModel(
        #     name='Letting',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('title', models.CharField(max_length=256)),
        #         ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
        #     ],
        # ),

        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Letting',
                    fields=[
                        ('id',
                         models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                          verbose_name='ID')),
                        ('title', models.CharField(max_length=256)),
                        ('address',
                         models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              to='lettings.Address')),
                    ],
                ),
            ],
            # Table already exists. See  oc_lettings_site/migrations/0003_auto_20210815_1634.py
            database_operations=[],
        ),
    ]
