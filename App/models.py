from django.db import models

# Create your models here.
# RESTAURANT MODEL.........................................................
class Restaurant(models.Model):
    rest_name = models.CharField(max_length = 300, unique = True)
    rest_location = models.CharField(max_length = 300)
    rest_logo = models.ImageField(upload_to = 'logos')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return str(self.rest_name)



# BOT MODEL.................................................
class Bot(models.Model):
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    bot_no = models.IntegerField()
    bot_name = models.CharField(max_length = 300)
    bot_color = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'bot_images')
    avialable = models.BooleanField(default=True, help_text="available or not avialabe for service")  # avialabe to serve or not avialable
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'
        ordering = ('-id',)

    def __str__(self):
        return (self.bot_name)


# VOICE BOT SETTINGS..............................................
class VBSettings(models.Model):
    username = models.CharField(max_length = 30, null = True, blank = True)
    time = models.DecimalField(max_digits=20, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Voice Bot Setting'
        verbose_name_plural = 'Voice Bot Settings'

    def __str__(self):
        return str(self.id)



# Mobile Settings ...............................................
class MobileSettings(models.Model):
    username = models.CharField(max_length = 30, null = True, blank = True)
    mob_no = models.CharField(max_length = 10)
    speaker = models.BooleanField(default = False)
    time = models.DecimalField(max_digits=20, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Mobile Setting'
        verbose_name_plural = 'Mobile Settings'

    def __str__(self):
        return str(self.id)

