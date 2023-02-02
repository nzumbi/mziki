from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
        return render(request, "mzikiapp/home.html")
        
def venues():
  # TODO: replace with real venues data.
  data = []
  groups = db.session.query(Venue.city, Venue.state).group_by(Venue.city, Venue.state).all()
  if not groups: 
    flash('no venues exists') 
    return render_template('pages/venues.html')
  for group in groups:
    venues = db.session.query(Venue).filter_by(city=group[0], state=group[1]).all()
    venues_list = [] # a list containig all venues for each group
    for venue in venues:
      venues_list.append({
        "id": venue.id,
        "name": venue.name,
        "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id == venue.id).filter(Show.start_time > datetime.now()).all())
      })
    data.append({
      "city":group[0],
      "state":group[1],
      "venues":venues_list,
    })
  return render_template('pages/venues.html', areas=data)

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



