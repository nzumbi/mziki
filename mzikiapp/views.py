from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
        return render(request, "mzikiapp/home.html")


def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # replace with real venue data from the venues table, using venue_id
  v = Venue.query.get(venue_id)
  data = {
    "id": v.id,
    "name": v.name,
    "genres": v.genres,
    "address": v.address,
    "city": v.city,
    "state": v.state,
    "phone": v.phone,
    "website": v.website,
    "facebook_link": v.facebook_link,
    "seeking_talent": v.seeking_talent,
    "seeking_description": v.seeking_description,
    "image_link": v.image_link,
    "past_shows": [],
    "upcoming_shows": [],
    "past_shows_count": 0,
    "upcoming_shows_count": 0,
  }



