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
import re

from allauth.account.models import EmailAddress
from allauth.account.views import EmailView
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Ride
from .forms import EnterRideForm


class ProfileView(LoginRequiredMixin, views.View):
    """A non-interactive view for displaying user data of the current logged user.

    Primary, at least for the moment, this contains a list of all rides that the user has entered. The rides are shown
    in a table and all distances are summed up.
    """

    """Handle a get request; fetches the corresponding rides from the DB and sums the distances."""
    def get(self, request):
        ride_list = Ride.objects.filter(user_id=request.user.id)
        total_kilometers = sum(map(lambda r: r.distance, ride_list))
        return render(request, 'profile.html', {
            'ride_list': ride_list,
            'total_kilometers': total_kilometers,
        })


class EnterRideView(LoginRequiredMixin, views.View):
    """The view that is presented to the user when entering ride data.

    This view contains a form with most of the fields of the Ride class (in fact all of the fields but the user). If the
    application receives a get request, the page is simply rendered. On a post request, meaning the user has hit the
    submit button, the form is validated and, if valid, a Ride object is created. After applying the current logged user
    to this new ride object, it is saved to the DB.
    """

    """Handle a get request; this renders the EnterRideForm into the enter_ride template."""
    def get(self, request):
        return render(request, 'enter_ride.html', {'form': EnterRideForm()})

    """Handle a post request.
    
    The form is validated and a new ride corresponding to the current user is saved to the DB.
    """
    def post(self, request):
        form = EnterRideForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(commit=False)
            ride = form.instance
            ride.user = request.user
            ride.save()
            return HttpResponseRedirect('/')


class CustomEmailView(EmailView):
    def post(self, request, *args, **kwargs):
        res = None
        if "action_add" in request.POST:
            res = super(CustomEmailView, self).post(request, *args, **kwargs)
        else:
            addresses = EmailAddress.objects.filter(user=request.user)
            request.POST = request.POST.copy()
            for action in request.POST:
                if re.match(r'^action_send_\d+$', str(action)):
                    idx = int(re.findall(r'_\d+$', str(action))[0][1:])
                    request.POST['email'] = addresses[idx].email
                    res = super(CustomEmailView, self)._action_send(request, *args, **kwargs)
                    break
                elif re.match(r'^action_remove_\d+$', str(action)):
                    idx = int(re.findall(r'_\d+$', str(action))[0][1:])
                    request.POST['email'] = addresses[idx].email
                    res = super(CustomEmailView, self)._action_remove(request, *args, **kwargs)
                    break
                elif re.match(r'^action_primary_\d+$', str(action)):
                    idx = int(re.findall(r'_\d+$', str(action))[0][1:])
                    print(str(idx) + '  --  ' + str(addresses))
                    request.POST['email'] = addresses[idx].email
                    res = super(CustomEmailView, self)._action_primary(request, *args, **kwargs)
                    break
            res = res or HttpResponseRedirect(self.success_url)
        return res
