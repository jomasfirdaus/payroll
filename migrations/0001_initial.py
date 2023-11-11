# Generated by Django 4.2.6 on 2023-11-07 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contract', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Gross Salary')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('social', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Social Security')),
                ('net', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_lock', models.BooleanField(default=False, null=True)),
                ('is_confirm', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salary', to='contract.contract')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Salarycreatedbys', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Salarydeletedbys', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salary', to='employee.employee')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Salaryupdatetedbys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '11-Data-Custom-Salary',
            },
            managers=[
                ('default_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]