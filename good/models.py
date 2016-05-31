from django.db import models
from django.contrib import admin
from user_profile.models import UserProfile
from django.contrib.auth.models import User

countries = (
    ("Afghanistan", "Afghanistan"),
    ("Albania", "Albania"),
    ("Algeria", "Algeria"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Antigua and Barbuda", "Antigua and Barbuda"),
    ("Argentina", "Argentina"),
    ("Armenia", "Armenia"),
    ("Aruba", "Aruba"),
    ("Australia", "Australia"),
    ("Austria", "Austria"),
    ("Azerbaijan", "Azerbaijan"),
    ("Bahamas, The", "Bahamas, The"),
    ("Bahrain", "Bahrain"),
    ("Bangladesh", "Bangladesh"),
    ("Barbados", "Barbados"),
    ("Belarus", "Belarus"),
    ("Belgium", "Belgium"),
    ("Belize", "Belize"),
    ("Benin", "Benin"),
    ("Bhutan", "Bhutan"),
    ("Bolivia", "Bolivia"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Botswana", "Botswana"),
    ("Brazil", "Brazil"),
    ("Brunei ", "Brunei "),
    ("Bulgaria", "Bulgaria"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burma", "Burma"),
    ("Burundi", "Burundi"),
    ("Cambodia", "Cambodia"),
    ("Cameroon", "Cameroon"),
    ("Canada", "Canada"),
    ("Cape Verde", "Cape Verde"),
    ("Central African Republic", "Central African Republic"),
    ("Chad", "Chad"),
    ("Chile", "Chile"),
    ("China", "China"),
    ("Colombia", "Colombia"),
    ("Comoros", "Comoros"),
    ("Congo, Democratic Republic of the", "Congo, Democratic Republic of the"),
    ("Congo, Republic of the", "Congo, Republic of the"),
    ("Costa Rica", "Costa Rica"),
    ("Cote d'Ivoire", "Cote d'Ivoire"),
    ("Croatia", "Croatia"),
    ("Cuba", "Cuba"),
    ("Curacao", "Curacao"),
    ("Cyprus", "Cyprus"),
    ("Czech Republic", "Czech Republic"),
    ("Denmark", "Denmark"),
    ("Djibouti", "Djibouti"),
    ("Dominica", "Dominica"),
    ("Dominican Republic", "Dominican Republic"),
    ("Ecuador", "Ecuador"),
    ("Egypt", "Egypt"),
    ("El Salvador", "El Salvador"),
    ("Equatorial Guinea", "Equatorial Guinea"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonia"),
    ("Ethiopia", "Ethiopia"),
    ("Fiji", "Fiji"),
    ("Finland", "Finland"),
    ("France", "France"),
    ("Gabon", "Gabon"),
    ("Gambia, The", "Gambia, The"),
    ("Georgia", "Georgia"),
    ("Germany", "Germany"),
    ("Ghana", "Ghana"),
    ("Greece", "Greece"),
    ("Grenada", "Grenada"),
    ("Guatemala", "Guatemala"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bissau"),
    ("Guyana", "Guyana"),
    ("Haiti", "Haiti"),
    ("Holy See", "Holy See"),
    ("Honduras", "Honduras"),
    ("Hong Kong", "Hong Kong"),
    ("Hungary", "Hungary"),
    ("Iceland", "Iceland"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Iran", "Iran"),
    ("Iraq", "Iraq"),
    ("Ireland", "Ireland"),
    ("Israel", "Israel"),
    ("Italy", "Italy"),
    ("Jamaica", "Jamaica"),
    ("Japan", "Japan"),
    ("Jordan", "Jordan"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kenya", "Kenya"),
    ("Kiribati", "Kiribati"),
    ("Korea, North", "Korea, North"),
    ("Korea, South", "Korea, South"),
    ("Kosovo", "Kosovo"),
    ("Kuwait", "Kuwait"),
    ("Kyrgyzstan", "Kyrgyzstan"),
    ("Laos", "Laos"),
    ("Latvia", "Latvia"),
    ("Lebanon", "Lebanon"),
    ("Lesotho", "Lesotho"),
    ("Liberia", "Liberia"),
    ("Libya", "Libya"),
    ("Liechtenstein", "Liechtenstein"),
    ("Lithuania", "Lithuania"),
    ("Luxembourg", "Luxembourg"),
    ("Macau", "Macau"),
    ("Macedonia", "Macedonia"),
    ("Madagascar", "Madagascar"),
    ("Malawi", "Malawi"),
    ("Malaysia", "Malaysia"),
    ("Maldives", "Maldives"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Marshall Islands", "Marshall Islands"),
    ("Mauritania", "Mauritania"),
    ("Mauritius", "Mauritius"),
    ("Mexico", "Mexico"),
    ("Micronesia", "Micronesia"),
    ("Moldova", "Moldova"),
    ("Monaco", "Monaco"),
    ("Mongolia", "Mongolia"),
    ("Montenegro", "Montenegro"),
    ("Morocco", "Morocco"),
    ("Mozambique", "Mozambique"),
    ("Namibia", "Namibia"),
    ("Nauru", "Nauru"),
    ("Nepal", "Nepal"),
    ("Netherlands", "Netherlands"),
    ("Netherlands Antilles", "Netherlands Antilles"),
    ("New Zealand", "New Zealand"),
    ("Nicaragua", "Nicaragua"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigeria"),
    ("North Korea", "North Korea"),
    ("Norway", "Norway"),
    ("Oman", "Oman"),
    ("Pakistan", "Pakistan"),
    ("Palau", "Palau"),
    ("Palestinian Territories", "Palestinian Territories"),
    ("Panama", "Panama"),
    ("Papua New Guinea", "Papua New Guinea"),
    ("Paraguay", "Paraguay"),
    ("Peru", "Peru"),
    ("Philippines", "Philippines"),
    ("Poland", "Poland"),
    ("Portugal", "Portugal"),
    ("Qatar", "Qatar"),
    ("Romania", "Romania"),
    ("Russia", "Russia"),
    ("Rwanda", "Rwanda"),
    ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
    ("Saint Lucia", "Saint Lucia"),
    ("Saint Vincent and the Grenadines", "Saint Vincent and the Grenadines"),
    ("Samoa ", "Samoa "),
    ("San Marino", "San Marino"),
    ("Sao Tome and Principe", "Sao Tome and Principe"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Senegal", "Senegal"),
    ("Serbia", "Serbia"),
    ("Seychelles", "Seychelles"),
    ("Sierra Leone", "Sierra Leone"),
    ("Singapore", "Singapore"),
    ("Sint Maarten", "Sint Maarten"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Solomon Islands", "Solomon Islands"),
    ("Somalia", "Somalia"),
    ("South Africa", "South Africa"),
    ("South Korea", "South Korea"),
    ("South Sudan", "South Sudan"),
    ("Spain ", "Spain "),
    ("Sri Lanka", "Sri Lanka"),
    ("Sudan", "Sudan"),
    ("Suriname", "Suriname"),
    ("Swaziland ", "Swaziland "),
    ("Sweden", "Sweden"),
    ("Switzerland", "Switzerland"),
    ("Syria", "Syria"),
    ("Taiwan", "Taiwan"),
    ("Tajikistan", "Tajikistan"),
    ("Tanzania", "Tanzania"),
    ("Thailand ", "Thailand "),
    ("Timor-Leste", "Timor-Leste"),
    ("Togo", "Togo"),
    ("Tonga", "Tonga"),
    ("Trinidad and Tobago", "Trinidad and Tobago"),
    ("Tunisia", "Tunisia"),
    ("Turkey", "Turkey"),
    ("Turkmenistan", "Turkmenistan"),
    ("Tuvalu", "Tuvalu"),
    ("Uganda", "Uganda"),
    ("Ukraine", "Ukraine"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("United Kingdom", "United Kingdom"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistan", "Uzbekistan"),
    ("Vanuatu", "Vanuatu"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Yemen", "Yemen"),
    ("Zambia", "Zambia"),
    ("Zimbabwe", "Zimbabwe"),
)

currencies = (
    ("USD", "USD"),
    ("EUR", "EURO"),
    ("RUB", "RUBLES"),
)


class Category(models.Model):
    class Meta:
        db_table = "categories"
        verbose_name_plural = "categories"

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent')
    list_filter = ('title', 'description', 'parent')


class Producer(models.Model):
    class Meta:
        db_table = "producers"

    title = models.CharField(max_length=50)
    country = models.CharField(choices=countries, max_length=100)
    description = models.TextField(max_length=500, null=True)

    def __unicode__(self):
        return self.title


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'description')
    list_filter = ('title', 'country', 'description')


def get_picture_path(instance, filename):
        return "%s\\%s" % (instance.title,  filename)


class Good(models.Model):
    class Meta:
        db_table = "goods"

    title = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    description = models.TextField(max_length=500, blank=True)
    category = models.ForeignKey(Category)
    currency = models.CharField(choices=currencies, max_length=100, default="USD")
    image = models.ImageField(upload_to=get_picture_path, null=True)

    def __unicode__(self):
        return "%s (%s) price: %d [rating %d]" % (self.title, self.producer, self.price, self.rating)


class GoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer', 'price', 'amount', 'rating', 'description', 'category', 'currency',
                    'image')
    list_filter = ('title', 'producer', 'price', 'amount', 'rating', 'description', 'category', 'currency',
                    'image')


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    good = models.ForeignKey(Good)
    text = models.TextField(max_length=500)
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField(null=True)
    user = models.ForeignKey(UserProfile, null=True)

    def __unicode__(self):
        return "%s: %s" % (self.pub_date, self.text)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('good', 'text', 'rating', 'pub_date', 'user')
    list_filter = ('good', 'text', 'rating', 'pub_date', 'user')


class Cart(models.Model):
    class Meta:
        db_table = "carts"

    user = models.ForeignKey(User)
    good = models.ForeignKey(Good)


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'good')
    list_filter = ('user', 'good')