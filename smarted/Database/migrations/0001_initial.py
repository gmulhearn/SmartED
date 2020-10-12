# Generated by Django 2.2.3 on 2020-10-12 01:12

import Database.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isDate', models.BooleanField(default=False)),
                ('date', models.DateTimeField(null=True)),
                ('dateDescription', models.CharField(max_length=255)),
                ('isPassFail', models.BooleanField(default=False)),
                ('weight', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mode', models.CharField(choices=[('E', 'EXTERNAL'), ('I', 'INTERNAL'), ('F', 'FLEXIBLE')], default='F', max_length=8)),
                ('semester', models.PositiveSmallIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('year', models.PositiveSmallIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1909), Database.models.max_value_current_year])),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isBlackboardGenerated', models.BooleanField()),
                ('blackboardLink', models.URLField()),
                ('dateAdded', models.DateTimeField(verbose_name='date published')),
                ('week', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completedVark', models.BooleanField(default=False)),
                ('V', models.DecimalField(decimal_places=4, max_digits=5, null=True)),
                ('A', models.DecimalField(decimal_places=4, max_digits=5, null=True)),
                ('R', models.DecimalField(decimal_places=4, max_digits=5, null=True)),
                ('K', models.DecimalField(decimal_places=4, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastModified', models.DateTimeField(null=True)),
                ('passFail', models.BooleanField(default=False)),
                ('value', models.DecimalField(decimal_places=4, max_digits=10)),
                ('goal', models.DecimalField(decimal_places=4, max_digits=10)),
                ('assessment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.AssessmentItem')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Database.User'),
        ),
        migrations.CreateModel(
            name='StaffCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Course')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.User'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.FileField(upload_to='uploads/')),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('feedback', models.TextField()),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Resource')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.User')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Institution'),
        ),
        migrations.AddField(
            model_name='assessmentitem',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Course'),
        ),
        migrations.CreateModel(
            name='ViewResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('viewTime', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Resource')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.User')),
            ],
            options={
                'unique_together': {('user', 'timestamp')},
            },
        ),
        migrations.CreateModel(
            name='CourseGradeGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.User')),
            ],
            options={
                'unique_together': {('user', 'course', 'grade')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'mode', 'semester', 'year')},
        ),
    ]
