#
# Biker, a biking competition website
# Copyright (C) 2019 surfingdmx <surfingdmx@tutanota.com>
#
# Biker is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# Biker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Biker. If not, see
# <https://www.gnu.org/licenses/>.
#

from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    """Extend the django user model by custom properties.

    The basic user model of django provides common features like name and email support, and other fields that are not
    used in this project (like age, address, phone number etc.). Because the register and login functionality (provided
    by django-allauth) relies on the presence of a common user class, the AbstractUser is extended.

    In order to work properly with other apps and replace/extends the standard django user implementation, this class
    has to be referenced to in the settings of the application, namely in the field AUTH_USER_MODEL.
    """

    """This field holds the sum of kilometers that the user has.
    
    In the future, when the data model is more elaborate, this field will (technically) not be necessary as the value
    can always be calculated as the sum of all rides. Still this field would probably improve performance if a user has
    a lot of rides. 
    """
    total_amount_of_kilometers = models.DecimalField(default=0.0, max_digits=7, decimal_places=1)


class Route(models.Model):
    """Provide shareable template for rides.

    A route is selectable by the user when he/she enters a ride. It saves them from looking up & typing the distance
    and automatically saves start and destination location (if the user wants to). Thus, the mandatory fields of a route
    is a (per-user) unique name and a distance. Optionally, the user can include the start and destination location.

    For the future there are plans to extend this class by geodata. This would mean that a user can save a GPS-track for
    a route.
    """

    """Associated user"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # TODO: unique for user only; should only be unique for user so independent user routes can have identical names
    """Name of the route serving as identifier."""
    name = models.CharField(max_length=200, unique=True)

    """The date the route was created"""
    creation_date = models.DateField(auto_now_add=True)

    """The date the route was last modified"""
    last_mod_date = models.DateField(auto_now=True)

    """Distance in kilometers with 1 decimal place"""
    distance = models.DecimalField(max_digits=4, decimal_places=1)

    """Name of the start location"""
    start_name = models.CharField(max_length=200, blank=True)

    """Name of the destination location"""
    destination_name = models.CharField(max_length=200, blank=True)

    """Short text for notes of the user"""
    note = models.CharField(max_length=200, blank=True)


class Ride(models.Model):
    """Represent a single ride of a user.

    This class combines the properties of a ride: the user who has completed it, the date, start time, end time,
    distance and a custom note.
    """

    """Associated user"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    """The date that the ride was taken on"""
    date = models.DateField(default=date.today)

    """The time that the ride was started"""
    start_time = models.TimeField(default=None, blank=True, null=True)

    """The time the ride was ended. This may be on the next day."""
    end_time = models.TimeField(default=None, blank=True, null=True)

    """The distance that was travelled, in kilometers with 1 decimal place."""
    distance = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    """Route that was taken; if not null, this eliminates the need for separate distance."""
    route = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)

    """A short text that the user may specify to recognize the ride later on."""
    note = models.CharField(max_length=200, blank=True)
