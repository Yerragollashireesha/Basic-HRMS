# Generated by Django 4.1.5 on 2024-02-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0028_gen_dt_budgetdatahistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gen_DT_ExpenseFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExpenseFrequencyEN', models.CharField(max_length=200)),
                ('ExpenseFrequencyRU', models.CharField(max_length=200)),
                ('ExpenseFrequencyTR', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['ExpenseFrequencyEN'],
            },
        ),
        migrations.CreateModel(
            name='Gen_DT_ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExpenseTypeEN', models.CharField(max_length=200)),
                ('ExpenseTypeRU', models.CharField(max_length=200)),
                ('ExpenseTypeTR', models.CharField(max_length=200)),
                ('ExpenseFrequency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.gen_dt_expensefrequency', verbose_name='Expense Frequency')),
            ],
            options={
                'ordering': ['ExpenseTypeEN'],
            },
        ),
    ]
