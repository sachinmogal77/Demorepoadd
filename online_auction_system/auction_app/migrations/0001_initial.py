# Generated by Django 4.1.3 on 2022-11-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllBids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AuctionDetails',
            fields=[
                ('auction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('auction_date', models.DateField(blank=True)),
                ('auction_start_time', models.TimeField(blank=True)),
                ('auction_end_time', models.TimeField(blank=True)),
                ('increment_amount', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AutomaticBidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_bid_amount', models.FloatField(blank=True)),
                ('inc_amount', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bidders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidder_type', models.CharField(choices=[('AUTOMATIC', 'automatic'), ('MANUAL', 'manual')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentBids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.FloatField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctionbids', to='auction_app.auctiondetails')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentbids', to='auction_app.bidders')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAuctions',
            fields=[
                ('current_auction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('auction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='current_auction', to='auction_app.auctiondetails')),
            ],
        ),
        migrations.CreateModel(
            name='ClosingBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closing_bid_amount', models.FloatField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='closing_auctions', to='auction_app.auctiondetails')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='closing_Bids', to='auction_app.bidders')),
            ],
        ),
    ]
