# Generated by Django 5.1.2 on 2024-11-04 17:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(max_length=20)),
                ('acc_no', models.CharField(max_length=15, unique=True)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('acc_type', models.CharField(choices=[('Saving', 'Saving'), ('Current', 'Current'), ('Overdraft', 'Overdraft')], max_length=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_from', models.IntegerField(default=0, editable=False)),
                ('amount_to', models.IntegerField(default=0, editable=False)),
                ('from_status', models.CharField(default='debited', editable=False, max_length=10)),
                ('to_status', models.CharField(default='credited', editable=False, max_length=10)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_from', to='accounts.account')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_to', to='accounts.account')),
            ],
        ),
    ]