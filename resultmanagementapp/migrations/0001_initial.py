# Generated by Django 4.1.3 on 2023-11-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('std_id', models.IntegerField()),
                ('present', models.BooleanField()),
                ('absent', models.BooleanField()),
                ('remarks', models.CharField(default='Good', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Course', max_length=45)),
                ('desc', models.CharField(default='Desc', max_length=45)),
                ('grade_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSubject',
            fields=[
                ('sub_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=200)),
                ('c_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('g_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='a', max_length=45)),
                ('desc', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('noticeheadline', models.CharField(max_length=100)),
                ('noticedescrip', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('pr_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='a', max_length=200)),
                ('fname', models.CharField(default='a', max_length=200)),
                ('lname', models.CharField(default='a', max_length=200)),
                ('dob', models.CharField(default='a', max_length=200)),
                ('phone', models.CharField(default='a', max_length=200)),
                ('mobile', models.CharField(default='a', max_length=200)),
                ('status', models.BooleanField()),
                ('password', models.CharField(max_length=45)),
                ('designation', models.CharField(default='Parent', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('photo', models.ImageField(default='no img', upload_to='pics')),
                ('Name', models.CharField(default='a', max_length=200)),
                ('Class', models.CharField(default='a', max_length=200)),
                ('RollNo', models.IntegerField(primary_key=True, serialize=False)),
                ('Percentage', models.CharField(default='a', max_length=200)),
                ('Reportsto', models.CharField(default='a', max_length=200)),
                ('email', models.CharField(default='a', max_length=200)),
                ('fname', models.CharField(default='a', max_length=200)),
                ('lname', models.CharField(default='a', max_length=200)),
                ('dob', models.CharField(default='a', max_length=200)),
                ('phone', models.CharField(default='a', max_length=200)),
                ('mobile', models.CharField(default='a', max_length=200)),
                ('p_id', models.IntegerField(unique=True)),
                ('status', models.BooleanField()),
                ('password', models.CharField(max_length=45)),
                ('designation', models.CharField(default='Student', max_length=45)),
                ('present', models.IntegerField(default=0)),
                ('absent', models.IntegerField(default=0)),
                ('c_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.CharField(default='a', max_length=200)),
                ('Sub1', models.CharField(max_length=200, null=True)),
                ('Sub2', models.CharField(max_length=200, null=True)),
                ('Sub3', models.CharField(max_length=200, null=True)),
                ('Sub4', models.CharField(max_length=200, null=True)),
                ('Sub5', models.CharField(max_length=200, null=True)),
                ('Sub1marks', models.CharField(max_length=200, null=True)),
                ('Sub2marks', models.CharField(max_length=200, null=True)),
                ('Sub3marks', models.CharField(max_length=200, null=True)),
                ('Sub4marks', models.CharField(max_length=200, null=True)),
                ('Sub5marks', models.CharField(max_length=200, null=True)),
                ('Sub1marksobt', models.CharField(max_length=200, null=True)),
                ('Sub2marksobt', models.CharField(max_length=200, null=True)),
                ('Sub3marksobt', models.CharField(max_length=200, null=True)),
                ('Sub4marksobt', models.CharField(max_length=200, null=True)),
                ('Sub5marksobt', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('assignee', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=50)),
                ('duedate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tr_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='a', max_length=200)),
                ('fname', models.CharField(default='a', max_length=200)),
                ('lname', models.CharField(default='a', max_length=200)),
                ('dob', models.CharField(default='a', max_length=200)),
                ('phone', models.CharField(default='a', max_length=200)),
                ('mobile', models.CharField(default='a', max_length=200)),
                ('status', models.BooleanField()),
                ('password', models.CharField(max_length=45)),
                ('designation', models.CharField(default='Teacher', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.CharField(max_length=1000)),
                ('refresh', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='a', max_length=200, unique=True)),
                ('password', models.CharField(default='a', max_length=200, unique=True)),
                ('designation', models.CharField(default='a', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.IntegerField()),
                ('name', models.CharField(default='a', max_length=45)),
                ('std_id', models.IntegerField()),
                ('c_id', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            options={
                'unique_together': {('std_id', 'exam_id')},
            },
        ),
        migrations.CreateModel(
            name='CourseSubjectMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.IntegerField()),
                ('std_id', models.IntegerField()),
                ('sub_name', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
            ],
            options={
                'unique_together': {('std_id', 'sub_name')},
            },
        ),
    ]
