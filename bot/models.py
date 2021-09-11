from django.db import models


# Create your models here.
class BotUser(models.Model):
    """
    model for storing the telegram user clicks count
    """
    FAT = 'fat'
    DUMB = 'dumb'
    STUPID = 'stupid'
    NO_JOKE = 'no_joke'
    JOKES = [
        (FAT, 'fat'),
        (DUMB, 'dump'),
        (STUPID, 'stupid'),
        (NO_JOKE, 'no_joke'),
    ]
    telegram_user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30, blank=True)
    count = models.IntegerField(null=True, blank=True, default=0)
    joke = models.CharField(choices=JOKES, max_length=30, default='no_joke')

    def __str__(self):
        return self.telegram_user_id
