# Generated by Django 3.0.4 on 2020-04-18 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='author')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('artist_image', models.ImageField(upload_to='artist')),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(default='default.jpeg', upload_to='genres')),
            ],
        ),
        migrations.CreateModel(
            name='ShareCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('share_image', models.ImageField(upload_to='share')),
                ('preview_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UgandanMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200, verbose_name='Song name')),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('song', models.FileField(upload_to='Files')),
                ('type', models.CharField(max_length=10)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('type_choice', models.CharField(choices=[('BI', 'Beat'), ('VI', 'Violin Piece'), ('GI', 'Guitar Piece'), ('PI', 'Piano piece'), ('VI', 'Vocal piece'), ('AI', 'African piece'), ('TI', 'Trumpet Piece'), ('SI', 'Saxaphone Piece')], max_length=2)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('top_100', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('sub_title', models.TextField(blank=True)),
                ('text', models.TextField()),
                ('sub_title1', models.TextField(blank=True)),
                ('sub_title2', models.TextField(blank=True)),
                ('sub_title3', models.TextField(blank=True)),
                ('sub_title4', models.TextField(blank=True)),
                ('sub_title5', models.TextField(blank=True)),
                ('sub_title6', models.TextField(blank=True)),
                ('sub_title7', models.TextField(blank=True)),
                ('sub_title8', models.TextField(blank=True)),
                ('sub_title9', models.TextField(blank=True)),
                ('sub_title10', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('description1', models.TextField(blank=True)),
                ('description2', models.TextField(blank=True)),
                ('description3', models.TextField(blank=True)),
                ('description4', models.TextField(blank=True)),
                ('description5', models.TextField(blank=True)),
                ('description6', models.TextField(blank=True)),
                ('description7', models.TextField(blank=True)),
                ('description8', models.TextField(blank=True)),
                ('description9', models.TextField(blank=True)),
                ('description10', models.TextField(blank=True)),
                ('description11', models.TextField(blank=True)),
                ('description12', models.TextField(blank=True)),
                ('description13', models.TextField(blank=True)),
                ('description14', models.TextField(blank=True)),
                ('description15', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='sharepost')),
                ('image1', models.ImageField(blank=True, upload_to='sharepost')),
                ('image2', models.ImageField(blank=True, upload_to='sharepost')),
                ('image3', models.ImageField(blank=True, upload_to='sharepost')),
                ('image4', models.ImageField(blank=True, upload_to='sharepost')),
                ('image5', models.ImageField(blank=True, upload_to='sharepost')),
                ('image6', models.ImageField(blank=True, upload_to='sharepost')),
                ('image7', models.ImageField(blank=True, upload_to='sharepost')),
                ('image8', models.ImageField(blank=True, upload_to='sharepost')),
                ('image9', models.ImageField(blank=True, upload_to='sharepost')),
                ('image10', models.ImageField(blank=True, upload_to='sharepost')),
                ('image11', models.ImageField(blank=True, upload_to='sharepost')),
                ('image12', models.ImageField(blank=True, upload_to='sharepost')),
                ('image13', models.ImageField(blank=True, upload_to='sharepost')),
                ('image14', models.ImageField(blank=True, upload_to='sharepost')),
                ('image15', models.ImageField(blank=True, upload_to='sharepost')),
                ('image16', models.ImageField(blank=True, upload_to='sharepost')),
                ('image17', models.ImageField(blank=True, upload_to='sharepost')),
                ('image18', models.ImageField(blank=True, upload_to='sharepost')),
                ('image19', models.ImageField(blank=True, upload_to='sharepost')),
                ('pdf', models.FileField(blank=True, upload_to='sharepostpdf')),
                ('pdf1', models.FileField(blank=True, upload_to='sharepostpdf')),
                ('pdf2', models.FileField(blank=True, upload_to='sharepostpdf')),
                ('pdf3', models.FileField(blank=True, upload_to='sharepostpdf')),
                ('audio1', models.FileField(blank=True, upload_to='sharepostaudio')),
                ('audio2', models.FileField(blank=True, upload_to='sharepostaudio')),
                ('audio3', models.FileField(blank=True, upload_to='sharepostaudio')),
                ('audio4', models.FileField(blank=True, upload_to='sharepostaudio')),
                ('video1', models.FileField(blank=True, upload_to='sharepostvideo')),
                ('video2', models.FileField(blank=True, upload_to='sharepostvideo')),
                ('video3', models.FileField(blank=True, upload_to='sharepostvideo')),
                ('video4', models.FileField(blank=True, upload_to='sharepostvideo')),
                ('star', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('about_author', models.ManyToManyField(to='blog.AboutAuthor')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('share_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.ShareCategory')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='Files')),
                ('content', models.CharField(max_length=40)),
                ('category_choice', models.CharField(blank=True, choices=[('Rb', 'Rnb'), ('Pp', 'Pop'), ('Dh', 'Danncehall'), ('Ab', 'Afrobeat'), ('RA', 'Regae'), ('AP', 'Afropop')], max_length=2)),
                ('type_choice', models.CharField(blank=True, choices=[('BI', 'Beat'), ('VI', 'Violin Piece'), ('GI', 'Guitar Piece'), ('PI', 'Piano piece'), ('VI', 'Vocal piece'), ('AI', 'African piece'), ('TI', 'Trumpet Piece'), ('SI', 'Saxaphone Piece')], max_length=2)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('made_with', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('template', models.FileField(blank=True, upload_to='products/')),
                ('demo', models.FileField(blank=True, upload_to='products/')),
                ('Signature_beat', models.FileField(blank=True, upload_to='products/')),
                ('plugins', models.CharField(max_length=100)),
                ('Your_country', django_countries.fields.CountryField(max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_ordered', models.BooleanField(default=False)),
                ('file_quantity', models.IntegerField(default=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('file_ordered', models.BooleanField(default=False)),
                ('demo_ordered', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.BillingAddress')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Payment')),
                ('posts', models.ManyToManyField(to='blog.OrderPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternationalMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200, verbose_name='Song name')),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('song', models.FileField(upload_to='Files')),
                ('type', models.CharField(max_length=10)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('type_choice', models.CharField(choices=[('BI', 'Beat'), ('VI', 'Violin Piece'), ('GI', 'Guitar Piece'), ('PI', 'Piano piece'), ('VI', 'Vocal piece'), ('AI', 'African piece'), ('TI', 'Trumpet Piece'), ('SI', 'Saxaphone Piece')], max_length=2)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('top_100', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='songs', to='blog.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Freestuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_id', models.TextField()),
                ('title', models.CharField(max_length=200, verbose_name='Song name')),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('song', models.FileField(upload_to='Files')),
                ('type', models.CharField(max_length=10)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('type_choice', models.CharField(choices=[('BI', 'Beat'), ('VI', 'Violin Piece'), ('GI', 'Guitar Piece'), ('PI', 'Piano piece'), ('VI', 'Vocal piece'), ('AI', 'African piece'), ('TI', 'Trumpet Piece'), ('SI', 'Saxaphone Piece')], max_length=2)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Freestuff')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Share')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
