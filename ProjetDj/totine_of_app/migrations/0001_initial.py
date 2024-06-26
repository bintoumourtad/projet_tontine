# Generated by Django 4.0 on 2024-03-28 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groupetontine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('cotisation_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frequence_despaiement', models.CharField(max_length=50)),
                ('date_decréation', models.DateField()),
            ],
        ),
       
    
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=25)),
                ('motdepasse', models.CharField(max_length=30)),
                ('date_naissance', models.DateTimeField(auto_now_add=True)),
                ('adress', models.CharField(max_length=20)),
                ('numero_telephon', models.CharField(max_length=20)),
            ],
        ),
    ]
