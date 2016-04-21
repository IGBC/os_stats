from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model that describes a user profile. Each profile is
    bound to a user and owns additional metadata such as a
    picture, biography text and gender.
    """

    # The UserProfile acts as a proxy to this Django user that handles all the authentication
    user = models.OneToOneField(User)
    description = models.TextField()
    dob = models.DateField('date of birth')
    location = models.CharField(max_length=32, default='Earth')
    gender = models.CharField(max_length=32, default='Unknown')
    # picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username


class OSDistribution(models.Model):
    name = models.CharField(max_length=64, default='')
    arch = models.CharField(max_length=16, default='amd64')


class Installation(models.Model):
    """
    A model that describes an installation with all the computer
    stats and some useful metadata.
    """

    UNKNOWN = 'Unknown'
    LINUX = 'Linux'
    BSD = 'BSD'
    WIN = 'Windows'
    OSX = 'Mac OS X'

    DESKTOP = 'Desktop'
    LAPTOP = 'Laptop'
    SERVER = 'Server'

    COMPUTER_TYPES = (
        (UNKNOWN, 'Unknown'),
        (DESKTOP, 'Desktop'),
        (LAPTOP, 'Laptop'),
        (SERVER, 'Server'),
    )

    OPERATING_SYSTEMS = (
        (UNKNOWN, 'Unknown'),
        (LINUX, 'Linux'),
        (BSD, 'BSD'),
        (WIN, 'Windows'),
        (OSX, 'Mac OS X'),
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
    type = models.CharField(max_length=16, choices=COMPUTER_TYPES, default=UNKNOWN) # TODO: Rename this to !type

    # Software running on it
    os = models.CharField(max_length=16, choices=OPERATING_SYSTEMS, default=UNKNOWN)
    distribution = models.ForeignKey(OSDistribution, blank=True, null=True)

    def __str__(self):
        return "Computer: %s with %s installed" % (self.name, str(self.os))
