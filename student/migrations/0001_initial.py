# Generated by Django 4.1.6 on 2023-02-13 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Address_1', models.CharField(max_length=255)),
                ('Address_2', models.CharField(max_length=255)),
                ('Guardian_Cell_phone', models.CharField(max_length=255)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='student_school_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_class', models.IntegerField()),
                ('Percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Commute', models.BooleanField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student_data')),
            ],
        ),
    ]
