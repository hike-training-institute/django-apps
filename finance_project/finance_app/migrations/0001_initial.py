# Generated by Django 2.1 on 2020-04-12 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowingDetail',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('borrowed_amount', models.FloatField(db_column='borrowed_amount')),
                ('borrowed_date', models.DateTimeField(db_column='borrowed_date')),
                ('interest_rate', models.FloatField(db_column='interest_rate')),
                ('interest_period', models.CharField(db_column='interest_period', max_length=255)),
                ('expected_return_date', models.DateTimeField(db_column='expected_return_date', null=True)),
                ('comments', models.TextField(blank=True, db_column='comments', null=True)),
            ],
            options={
                'db_table': 'borrowing_detail',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BorrowingHistory',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('borrowed_detail', models.ForeignKey(db_column='borrowed_detail', on_delete=django.db.models.deletion.CASCADE, to='finance_app.BorrowingDetail')),
            ],
            options={
                'db_table': 'borrowing_history',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LendingDetail',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('lending_amount', models.FloatField(db_column='lending_amount')),
                ('lending_date', models.DateTimeField(db_column='lending_date')),
                ('interest_rate', models.FloatField(db_column='interest_rate')),
                ('interest_period', models.CharField(db_column='interest_period', max_length=255)),
                ('expected_return_date', models.DateTimeField(db_column='expected_return_date', null=True)),
                ('comments', models.TextField(blank=True, db_column='comments', null=True)),
            ],
            options={
                'db_table': 'lending_detail',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LendingHistory',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'lending_history',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('tenant_id', models.IntegerField(db_column='tenant_id')),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('dob', models.DateField(db_column='dob')),
                ('age', models.IntegerField(db_column='age')),
                ('phone_number', models.IntegerField(db_column='phone_number')),
                ('address', models.TextField(db_column='address')),
                ('created_time', models.DateTimeField(db_column='created_time')),
                ('modified_time', models.DateTimeField(db_column='modified_time')),
                ('deleted_time', models.DateTimeField(db_column='deleted_time')),
            ],
            options={
                'db_table': 'personal_detail',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('role', models.CharField(db_column='role', max_length=255)),
            ],
            options={
                'db_table': 'roles',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('created_time', models.DateTimeField(db_column='created_time')),
                ('status', models.BooleanField(db_column='status', default=True)),
                ('modified_time', models.DateTimeField(db_column='modified_time')),
                ('deleted_time', models.DateTimeField(db_column='deleted_time')),
            ],
            options={
                'db_table': 'tenant',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='role',
            field=models.ForeignKey(db_column='role', on_delete=django.db.models.deletion.CASCADE, to='finance_app.Roles'),
        ),
        migrations.AddField(
            model_name='lendinghistory',
            name='lended_by',
            field=models.ForeignKey(db_column='lended_by', on_delete=django.db.models.deletion.CASCADE, to='finance_app.PersonalDetail'),
        ),
        migrations.AddField(
            model_name='lendinghistory',
            name='lended_detail',
            field=models.ForeignKey(db_column='lended_detail', on_delete=django.db.models.deletion.CASCADE, to='finance_app.LendingDetail'),
        ),
        migrations.AddField(
            model_name='lendingdetail',
            name='leneded_to',
            field=models.ForeignKey(db_column='lended_to', on_delete=django.db.models.deletion.CASCADE, to='finance_app.PersonalDetail'),
        ),
        migrations.AddField(
            model_name='borrowinghistory',
            name='borrowed_from',
            field=models.ForeignKey(db_column='borrowed_from', on_delete=django.db.models.deletion.CASCADE, to='finance_app.PersonalDetail'),
        ),
        migrations.AddField(
            model_name='borrowingdetail',
            name='borrowed_to',
            field=models.ForeignKey(db_column='borrowed_to', on_delete=django.db.models.deletion.CASCADE, to='finance_app.PersonalDetail'),
        ),
    ]
