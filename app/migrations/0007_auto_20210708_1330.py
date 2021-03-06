# Generated by Django 3.2.5 on 2021-07-08 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20210708_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharing_type', models.CharField(blank=True, choices=[('p', 'Permanent'), ('t', 'Time based Share')], default='p', help_text='Book availability', max_length=1)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='app.book')),
                ('share_to_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['due_back', 'sharing_type'],
            },
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]
