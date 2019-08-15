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

from django.contrib.auth.models import AbstractUser
from django.db import models


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
