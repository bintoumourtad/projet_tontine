# Generated by Django 4.0 on 2019-01-01 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0004_alter_groupetontinee_cotisation_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contributions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_contribution', models.CharField(max_length=150)),
                ('date_contribution', models.DateTimeField()),
                ('groupe_tontine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totine_of_app.groupetontinee')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totine_of_app.user')),
            ],
        ),
    ]
