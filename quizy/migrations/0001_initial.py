# Generated by Django 4.0 on 2021-12-19 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام شرکت کننده')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل شرکت کننده')),
                ('phone_number', models.CharField(max_length=11, verbose_name='تلفن شرکت کننده')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_question', models.CharField(max_length=500, verbose_name='سوال')),
                ('category', models.CharField(choices=[('A', 'فرهنگی'), ('B', 'اجتماعی'), ('C', 'سیاسی'), ('D', 'اقتصادی'), ('E', 'ورزشی')], max_length=5, verbose_name='گروه سوالات')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_question', models.CharField(max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizy.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_a', models.CharField(max_length=500, verbose_name='Option A')),
                ('option_b', models.CharField(max_length=500, verbose_name='Option B')),
                ('option_c', models.CharField(max_length=500, verbose_name='Option C')),
                ('option_d', models.CharField(max_length=500, verbose_name='Option D')),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizy.question')),
            ],
        ),
    ]
