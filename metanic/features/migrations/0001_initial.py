# Generated by Django 2.1 on 2018-08-06 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('identifier', models.SlugField(blank=True, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ('created', 'last_modified'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeatureUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='features.Feature')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ('created', 'last_modified'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created', 'last_modified'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BooleanFeatureValue',
            fields=[
                ('featurevalue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='features.FeatureValue')),
                ('value', models.BooleanField()),
            ],
            options={
                'ordering': ('created', 'last_modified'),
                'abstract': False,
            },
            bases=('features.featurevalue',),
        ),
        migrations.CreateModel(
            name='NumericFeatureValue',
            fields=[
                ('featurevalue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='features.FeatureValue')),
                ('value', models.DecimalField(decimal_places=3, max_digits=11)),
            ],
            options={
                'ordering': ('created', 'last_modified'),
                'abstract': False,
            },
            bases=('features.featurevalue',),
        ),
        migrations.CreateModel(
            name='StringFeatureValue',
            fields=[
                ('featurevalue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='features.FeatureValue')),
                ('value', models.TextField()),
            ],
            options={
                'ordering': ('created', 'last_modified'),
                'abstract': False,
            },
            bases=('features.featurevalue',),
        ),
        migrations.AddField(
            model_name='featureusage',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='features.FeatureValue'),
        ),
    ]
