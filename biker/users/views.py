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

from .models import Ride, Route
from .forms import EnterRideForm, EnterRouteForm


class ProfileView(LoginRequiredMixin, views.View):
    """A non-interactive view for displaying user data of the current logged user.

    Non-interactive means that there is no form on the page where the user can enter any data. There are links to the
    corresponding locations if the user wants to enter data.
    """

    """Handle a get request; fetches the most recent rides of the user for displaying them in a table."""
    def get(self, request):
        ride_list = Ride.objects.filter(user_id=request.user.id).order_by('date', 'start_time')[:10]
        route_list = Route.objects.filter(user_id=request.user.id).order_by('name')[:10]
        return render(request, 'profile.html', {
            'ride_list': ride_list,
            'route_list': route_list,
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
        route_list = Route.objects.filter(user_id=request.user.id).order_by('name')
        return render(request, 'enter_ride.html', {'route_list': route_list})

    """Handle a post request.
    
    The form is validated and a new ride corresponding to the current user is saved to the DB.
    """
    def post(self, request):
        form = EnterRideForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(commit=False)
            ride = form.instance
            ride.user = request.user
            if request.POST['route-dist'] == 'route':
                ride.route = Route.objects.get(user_id=request.user.id, name=request.POST['route'])
                ride.distance = None
            elif request.POST['route-dist'] == 'dist':
                ride.distance = request.POST['distance']
                ride.route = None
            ride.save()
            return HttpResponseRedirect('/')


class EnterRouteView(LoginRequiredMixin, views.View):
    """The view that is presented to the user when entering a route."""

    """Handle a get request; this renders the EnterRouteForm into the enter_route template."""
    def get(self, request):
        return render(request, 'enter_route.html')

    """Handle a post request."""
    def post(self, request):
        form = EnterRouteForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(commit=False)
            route = form.instance
            route.user = request.user
            route.save()
            return HttpResponseRedirect('/')
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
                    request.POST['email'] = addresses[idx].email
                    res = super(CustomEmailView, self)._action_primary(request, *args, **kwargs)
                    break
            res = res or HttpResponseRedirect(self.success_url)
        return res
