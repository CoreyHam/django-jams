# Generated by Django 4.0.4 on 2022-04-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams_library', '0002_remove_album_artist_remove_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(to='jams_library.artist'),
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(to='jams_library.album'),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='jams_library.artist'),
        ),
    ]
