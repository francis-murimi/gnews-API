# Generated by Django 4.1 on 2022-08-19 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_churchmembership_comment_and_more'),
        ('product', '0002_alter_topic_options_topic_church_alter_blog_church_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.churchitem'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]