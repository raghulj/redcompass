from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from compass.models import Compass
import json
from django.http import HttpResponse
from django.utils import timezone

from utils import opencellid


def index(request):
    latest_poll_list = Compass.objects.order_by('-last_ping')[:10]
    context = {'output': latest_poll_list}
    return render(request, 'compass/index.html', context)

@csrf_exempt
def update_location(request):
	mcc = request.POST.get("mcc", "")
	mnc = request.POST.get("mnc", "")
	lac = request.POST.get("lac", "")
	cellid = request.POST.get("cellid", "")

	data = opencellid.get_coordinates(mcc, mnc,lac, cellid)
	print data
	if not data:
                to_json = {
                "success": "not"
                }
 		return HttpResponse(json.dumps(to_json), mimetype='application/json')

	lat = data[0]
	lon = data [1]
	if lat and lon:
		compass = Compass(latitude=lat,longitude=lon, last_ping=timezone.now())
		compass.save()
		to_json = {
		"success": "ok",
		"lat" : lat,
		"lon" : lon
		}
	else:
		to_json = {
		"success": "not"
		}

	return HttpResponse(json.dumps(to_json), mimetype='application/json')
