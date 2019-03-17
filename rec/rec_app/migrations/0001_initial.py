# Generated by Django 2.1.4 on 2019-03-16 08:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_department', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_interest', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.IntegerField(max_length=8, validators=[django.core.validators.RegexValidator('\\d{8,8}', 'Registration Number must be 8 digits', 'Invalid Registration Number')])),
                ('phone', models.IntegerField(max_length=10, validators=[django.core.validators.RegexValidator('\\d{10,10}', 'Number must be 10 digits', 'Invalid number')])),
                ('hostel', models.CharField(max_length=20)),
                ('room_no', models.IntegerField(max_length=5)),
                ('cgpa', models.FloatField(default=None)),
                ('year', models.IntegerField(max_length=4)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rec_app.Department')),
                ('interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rec_app.Interest')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_skills', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='recruitment',
            name='skills',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rec_app.Skills'),
        ),
    ]
