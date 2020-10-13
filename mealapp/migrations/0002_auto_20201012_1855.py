# Generated by Django 2.0.3 on 2020-10-12 12:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='Aboutus/')),
                ('Speach', ckeditor.fields.RichTextField()),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'About_us',
                'verbose_name_plural': 'About_us',
            },
        ),
        migrations.CreateModel(
            name='AddAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('add_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Add Amount',
                'verbose_name_plural': 'Add Amounts',
            },
        ),
        migrations.CreateModel(
            name='AddBazar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('total_bazar', models.CharField(max_length=20)),
                ('bazar_date', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Add Bazar',
                'verbose_name_plural': 'Add Bazars',
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=50)),
                ('mail', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('Image', models.ImageField(upload_to='Agents/')),
                ('Facebook', models.CharField(blank=True, max_length=100)),
                ('Twitter', models.CharField(blank=True, max_length=100)),
                ('linkdin', models.CharField(blank=True, max_length=100)),
                ('google_plas', models.CharField(blank=True, max_length=100)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.FileField(upload_to='blog/')),
                ('image2', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('image3', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('image4', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('image5', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('title', models.CharField(max_length=200)),
                ('discription', ckeditor.fields.RichTextField()),
                ('author', models.CharField(blank=True, max_length=100)),
                ('seo_title', models.TextField(blank=True)),
                ('seo_discription', models.TextField(blank=True)),
                ('seo_keyword', models.TextField(blank=True)),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('Status', models.BooleanField(default=True)),
                ('view', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categores',
            },
        ),
        migrations.CreateModel(
            name='company_footer_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('facebook', models.TextField(max_length=254)),
                ('tweeter', models.TextField(blank=True, max_length=254)),
                ('google_plas', models.TextField(blank=True, max_length=254)),
                ('youtube', models.TextField(blank=True, max_length=254)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'company_footer_link',
                'verbose_name_plural': 'company_footer_link',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=254)),
                ('Designation', models.TextField(blank=True, max_length=254)),
                ('Phone_number', models.CharField(max_length=50)),
                ('Mail', models.EmailField(max_length=254)),
                ('Address', models.TextField(max_length=254)),
                ('Website', models.TextField(blank=True, max_length=254)),
                ('Facebook', models.TextField(blank=True, max_length=254)),
                ('Speach', ckeditor.fields.RichTextField(blank=True)),
                ('google_map', models.TextField(blank=True)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='DailyMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_meal', models.IntegerField()),
                ('add_date', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Daily Meal',
                'verbose_name_plural': 'Daily Meals',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Image', models.ImageField(blank=True, upload_to='logo/')),
                ('icon', models.ImageField(blank=True, upload_to='logo/')),
                ('Status', models.BooleanField(default=True)),
                ('header_image', models.ImageField(blank=True, upload_to='logo/')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
            },
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=60)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('room_no', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('admit_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Member Info',
                'verbose_name_plural': 'Members Info',
            },
        ),
        migrations.CreateModel(
            name='Properte',
            fields=[
                ('image1', models.ImageField(upload_to='property/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='property/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='property/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='property/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='property/')),
                ('title', models.CharField(max_length=200)),
                ('area', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, default=0, max_length=20)),
                ('discription', ckeditor.fields.RichTextField()),
                ('feature1', models.CharField(max_length=50)),
                ('feature2', models.CharField(blank=True, max_length=50)),
                ('feature3', models.CharField(blank=True, max_length=50)),
                ('feature4', models.CharField(blank=True, max_length=50)),
                ('feature5', models.CharField(blank=True, max_length=50)),
                ('feature6', models.CharField(blank=True, max_length=50)),
                ('feature7', models.CharField(blank=True, max_length=50)),
                ('feature8', models.CharField(blank=True, max_length=50)),
                ('feature9', models.CharField(blank=True, max_length=50)),
                ('feature10', models.CharField(blank=True, max_length=50)),
                ('feature11', models.CharField(blank=True, max_length=50)),
                ('feature12', models.CharField(blank=True, max_length=50)),
                ('feature13', models.CharField(blank=True, max_length=50)),
                ('feature14', models.CharField(blank=True, max_length=50)),
                ('feature15', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(max_length=250)),
                ('gmap', models.TextField(blank=True)),
                ('contact_name', models.CharField(blank=True, max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=250)),
                ('seo_discription', models.TextField(blank=True)),
                ('seo_keyword', models.TextField(blank=True)),
                ('seo_title', models.TextField(blank=True)),
                ('propertyID', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.BooleanField(default=False)),
                ('feature_property', models.BooleanField(default=False)),
                ('view', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealapp.Category')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Propertes',
            },
        ),
        migrations.CreateModel(
            name='SeoContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_meta_title', models.TextField(blank=True)),
                ('index_meta_description', models.TextField(blank=True)),
                ('index_meta_keywords', models.TextField(blank=True)),
                ('blog_title', models.TextField(blank=True)),
                ('blog_description', models.TextField(blank=True)),
                ('blog_keywords', models.TextField(blank=True)),
                ('contact_title', models.TextField(blank=True)),
                ('contact_description', models.TextField(blank=True)),
                ('contact_keywords', models.TextField(blank=True)),
                ('properties_title', models.TextField(blank=True)),
                ('properties_description', models.TextField(blank=True)),
                ('properties_keywords', models.TextField(blank=True)),
                ('about_us_title', models.TextField(blank=True)),
                ('about_us_description', models.TextField(blank=True)),
                ('about_us_keywords', models.TextField(blank=True)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'SeoContent',
                'verbose_name_plural': 'SeoContents',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Icon', models.CharField(max_length=50)),
                ('Details', ckeditor.fields.RichTextField()),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slider/')),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='speach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Details', ckeditor.fields.RichTextField()),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'speach',
                'verbose_name_plural': 'speach',
            },
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategores',
            },
        ),
        migrations.CreateModel(
            name='user_massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('subject', models.TextField(blank=True)),
                ('massage', ckeditor.fields.RichTextField()),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'user_massage',
                'verbose_name_plural': 'user_massages',
            },
        ),
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'user_reg',
                'verbose_name_plural': 'user_reg',
            },
        ),
        migrations.DeleteModel(
            name='AddMember',
        ),
        migrations.AddField(
            model_name='properte',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealapp.subcategory'),
        ),
        migrations.AddField(
            model_name='properte',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealapp.user_reg'),
        ),
        migrations.AddField(
            model_name='dailymeal',
            name='member_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealapp.MemberInfo'),
        ),
        migrations.AddField(
            model_name='addamount',
            name='member_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealapp.MemberInfo'),
        ),
    ]
