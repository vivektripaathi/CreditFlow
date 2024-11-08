from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('monthly_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('approved_limit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
