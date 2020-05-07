from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = Visit.get_duration(visit)
        data = {
            "entered_at": visit.entered_at,
            "duration": Visit.format_duration(duration),
            "is_strange": Visit.is_visit_long(visit)
            }
        this_passcard_visits.append(data)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
