from django.db import models
from django.contrib.auth.models import User


class EnumField(models.Field):
    """
    A field class that maps to MySQL's ENUM type.

    Usage:

    class Card(models.Model):
        suit = EnumField(values=('Clubs', 'Diamonds', 'Spades', 'Hearts'))

    c = Card()
    c.suit = 'Clubs'
    c.save()
    """

    def __init__(self, *args, **kwargs):
        self.values = kwargs.pop('values')
        kwargs['choices'] = [(v, v) for v in self.values]
        kwargs['default'] = self.values[0]
        super(EnumField, self).__init__(*args, **kwargs)

    def db_type(self):
        return "enum({0})".format(','.join("'%s'" % v for v in self.values))


class UserProfile(models.Model):
    """
    A model that describes a user profile. Each profile is
    bound to a user and owns additional metadata such as a
    picture, biography text and gender.
    """

    user = models.OneToOneField(User)
    description = models.TextField()
    dob = models.DateField('date of birth')
    location = models.CharField(max_length=32, default='Earth')
    gender = models.CharField(max_length=32, default='Unknown')
    # picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username


class Installation(models.Model):
    """
    A model that describes an installation with all the computer
    stats and some useful metadata.
    """

    OS_TYPES = (
        (0, 'Unknown'),
        (1, 'Linux'),
        (2, 'BSD'),
        (3, 'Windows'),
        (4, 'Mac OS X'),
    )

    MACHINE_TYPE = (
        (0, 'Unknown'),
        (1, 'Desktop'),
        (2, 'Laptop'),
        (3, 'Server'),
    )

    name = models.CharField(max_length=32, default='My Computer')
    date_created = models.DateTimeField('date created')
    last_seen = models.DateTimeField('date modified')
    owner = models.ForeignKey(UserProfile, blank=True, null=True)

    # Machine details
    cpu = models.CharField(max_length=128, default='Unknown')
    mem_type = models.CharField(max_length=16, default='Unknown')
    mem_amount = models.IntegerField(default=0)
    gpu = models.CharField(max_length=64, default='Unknown')
    os = models.IntegerField(choices=OS_TYPES, default=0)
    type = models.IntegerField(choices=MACHINE_TYPE, default=0)

    def __str__(self):
        return "Computer: %s with %s installed" % (self.name, str(self.os))
