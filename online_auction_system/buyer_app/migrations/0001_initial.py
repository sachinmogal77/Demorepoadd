# Generated by Django 4.1.3 on 2022-11-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_wishlist', to='auction_app.auctiondetails')),
            ],
        ),
    ]
