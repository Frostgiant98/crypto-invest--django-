# Generated by Django 3.1 on 2022-02-20 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='withdrawal',
            fields=[
                ('withdrawal_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=10)),
                ('withdrawal_account', models.CharField(max_length=40)),
                ('withdrawal_wallet', models.CharField(max_length=40)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('Personal', 'Personal'), ('Business', 'Business'), ('Retirement', 'Retirement')], default='Personal', max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=100, null=True)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('wallet', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=16)),
                ('message', models.TextField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='deposits',
            fields=[
                ('deposit_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=40)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
