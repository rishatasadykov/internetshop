# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('parent', models.ForeignKey(blank=True, to='good.Category', null=True)),
            ],
            options={
                'db_table': 'categories',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=500)),
                ('rating', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=500, blank=True)),
                ('currency', models.CharField(default=b'USD', max_length=100, choices=[(b'USD', b'USD'), (b'EUR', b'EURO'), (b'RUB', b'RUBLES')])),
                ('category', models.ForeignKey(to='good.Category')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100, choices=[(b'Afghanistan', b'Afghanistan'), (b'Albania', b'Albania'), (b'Algeria', b'Algeria'), (b'Andorra', b'Andorra'), (b'Angola', b'Angola'), (b'Antigua and Barbuda', b'Antigua and Barbuda'), (b'Argentina', b'Argentina'), (b'Armenia', b'Armenia'), (b'Aruba', b'Aruba'), (b'Australia', b'Australia'), (b'Austria', b'Austria'), (b'Azerbaijan', b'Azerbaijan'), (b'Bahamas, The', b'Bahamas, The'), (b'Bahrain', b'Bahrain'), (b'Bangladesh', b'Bangladesh'), (b'Barbados', b'Barbados'), (b'Belarus', b'Belarus'), (b'Belgium', b'Belgium'), (b'Belize', b'Belize'), (b'Benin', b'Benin'), (b'Bhutan', b'Bhutan'), (b'Bolivia', b'Bolivia'), (b'Bosnia and Herzegovina', b'Bosnia and Herzegovina'), (b'Botswana', b'Botswana'), (b'Brazil', b'Brazil'), (b'Brunei ', b'Brunei '), (b'Bulgaria', b'Bulgaria'), (b'Burkina Faso', b'Burkina Faso'), (b'Burma', b'Burma'), (b'Burundi', b'Burundi'), (b'Cambodia', b'Cambodia'), (b'Cameroon', b'Cameroon'), (b'Canada', b'Canada'), (b'Cape Verde', b'Cape Verde'), (b'Central African Republic', b'Central African Republic'), (b'Chad', b'Chad'), (b'Chile', b'Chile'), (b'China', b'China'), (b'Colombia', b'Colombia'), (b'Comoros', b'Comoros'), (b'Congo, Democratic Republic of the', b'Congo, Democratic Republic of the'), (b'Congo, Republic of the', b'Congo, Republic of the'), (b'Costa Rica', b'Costa Rica'), (b"Cote d'Ivoire", b"Cote d'Ivoire"), (b'Croatia', b'Croatia'), (b'Cuba', b'Cuba'), (b'Curacao', b'Curacao'), (b'Cyprus', b'Cyprus'), (b'Czech Republic', b'Czech Republic'), (b'Denmark', b'Denmark'), (b'Djibouti', b'Djibouti'), (b'Dominica', b'Dominica'), (b'Dominican Republic', b'Dominican Republic'), (b'Ecuador', b'Ecuador'), (b'Egypt', b'Egypt'), (b'El Salvador', b'El Salvador'), (b'Equatorial Guinea', b'Equatorial Guinea'), (b'Eritrea', b'Eritrea'), (b'Estonia', b'Estonia'), (b'Ethiopia', b'Ethiopia'), (b'Fiji', b'Fiji'), (b'Finland', b'Finland'), (b'France', b'France'), (b'Gabon', b'Gabon'), (b'Gambia, The', b'Gambia, The'), (b'Georgia', b'Georgia'), (b'Germany', b'Germany'), (b'Ghana', b'Ghana'), (b'Greece', b'Greece'), (b'Grenada', b'Grenada'), (b'Guatemala', b'Guatemala'), (b'Guinea', b'Guinea'), (b'Guinea-Bissau', b'Guinea-Bissau'), (b'Guyana', b'Guyana'), (b'Haiti', b'Haiti'), (b'Holy See', b'Holy See'), (b'Honduras', b'Honduras'), (b'Hong Kong', b'Hong Kong'), (b'Hungary', b'Hungary'), (b'Iceland', b'Iceland'), (b'India', b'India'), (b'Indonesia', b'Indonesia'), (b'Iran', b'Iran'), (b'Iraq', b'Iraq'), (b'Ireland', b'Ireland'), (b'Israel', b'Israel'), (b'Italy', b'Italy'), (b'Jamaica', b'Jamaica'), (b'Japan', b'Japan'), (b'Jordan', b'Jordan'), (b'Kazakhstan', b'Kazakhstan'), (b'Kenya', b'Kenya'), (b'Kiribati', b'Kiribati'), (b'Korea, North', b'Korea, North'), (b'Korea, South', b'Korea, South'), (b'Kosovo', b'Kosovo'), (b'Kuwait', b'Kuwait'), (b'Kyrgyzstan', b'Kyrgyzstan'), (b'Laos', b'Laos'), (b'Latvia', b'Latvia'), (b'Lebanon', b'Lebanon'), (b'Lesotho', b'Lesotho'), (b'Liberia', b'Liberia'), (b'Libya', b'Libya'), (b'Liechtenstein', b'Liechtenstein'), (b'Lithuania', b'Lithuania'), (b'Luxembourg', b'Luxembourg'), (b'Macau', b'Macau'), (b'Macedonia', b'Macedonia'), (b'Madagascar', b'Madagascar'), (b'Malawi', b'Malawi'), (b'Malaysia', b'Malaysia'), (b'Maldives', b'Maldives'), (b'Mali', b'Mali'), (b'Malta', b'Malta'), (b'Marshall Islands', b'Marshall Islands'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Mexico', b'Mexico'), (b'Micronesia', b'Micronesia'), (b'Moldova', b'Moldova'), (b'Monaco', b'Monaco'), (b'Mongolia', b'Mongolia'), (b'Montenegro', b'Montenegro'), (b'Morocco', b'Morocco'), (b'Mozambique', b'Mozambique'), (b'Namibia', b'Namibia'), (b'Nauru', b'Nauru'), (b'Nepal', b'Nepal'), (b'Netherlands', b'Netherlands'), (b'Netherlands Antilles', b'Netherlands Antilles'), (b'New Zealand', b'New Zealand'), (b'Nicaragua', b'Nicaragua'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'North Korea', b'North Korea'), (b'Norway', b'Norway'), (b'Oman', b'Oman'), (b'Pakistan', b'Pakistan'), (b'Palau', b'Palau'), (b'Palestinian Territories', b'Palestinian Territories'), (b'Panama', b'Panama'), (b'Papua New Guinea', b'Papua New Guinea'), (b'Paraguay', b'Paraguay'), (b'Peru', b'Peru'), (b'Philippines', b'Philippines'), (b'Poland', b'Poland'), (b'Portugal', b'Portugal'), (b'Qatar', b'Qatar'), (b'Romania', b'Romania'), (b'Russia', b'Russia'), (b'Rwanda', b'Rwanda'), (b'Saint Kitts and Nevis', b'Saint Kitts and Nevis'), (b'Saint Lucia', b'Saint Lucia'), (b'Saint Vincent and the Grenadines', b'Saint Vincent and the Grenadines'), (b'Samoa ', b'Samoa '), (b'San Marino', b'San Marino'), (b'Sao Tome and Principe', b'Sao Tome and Principe'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Senegal', b'Senegal'), (b'Serbia', b'Serbia'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Singapore', b'Singapore'), (b'Sint Maarten', b'Sint Maarten'), (b'Slovakia', b'Slovakia'), (b'Slovenia', b'Slovenia'), (b'Solomon Islands', b'Solomon Islands'), (b'Somalia', b'Somalia'), (b'South Africa', b'South Africa'), (b'South Korea', b'South Korea'), (b'South Sudan', b'South Sudan'), (b'Spain ', b'Spain '), (b'Sri Lanka', b'Sri Lanka'), (b'Sudan', b'Sudan'), (b'Suriname', b'Suriname'), (b'Swaziland ', b'Swaziland '), (b'Sweden', b'Sweden'), (b'Switzerland', b'Switzerland'), (b'Syria', b'Syria'), (b'Taiwan', b'Taiwan'), (b'Tajikistan', b'Tajikistan'), (b'Tanzania', b'Tanzania'), (b'Thailand ', b'Thailand '), (b'Timor-Leste', b'Timor-Leste'), (b'Togo', b'Togo'), (b'Tonga', b'Tonga'), (b'Trinidad and Tobago', b'Trinidad and Tobago'), (b'Tunisia', b'Tunisia'), (b'Turkey', b'Turkey'), (b'Turkmenistan', b'Turkmenistan'), (b'Tuvalu', b'Tuvalu'), (b'Uganda', b'Uganda'), (b'Ukraine', b'Ukraine'), (b'United Arab Emirates', b'United Arab Emirates'), (b'United Kingdom', b'United Kingdom'), (b'Uruguay', b'Uruguay'), (b'Uzbekistan', b'Uzbekistan'), (b'Vanuatu', b'Vanuatu'), (b'Venezuela', b'Venezuela'), (b'Vietnam', b'Vietnam'), (b'Yemen', b'Yemen'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe')])),
                ('description', models.TextField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'producers',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='producer',
            field=models.ForeignKey(to='good.Producer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='good',
            field=models.ForeignKey(to='good.Good'),
        ),
        migrations.AddField(
            model_name='cart',
            name='good',
            field=models.ForeignKey(to='good.Good'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='user_profile.UserProfile'),
        ),
    ]
