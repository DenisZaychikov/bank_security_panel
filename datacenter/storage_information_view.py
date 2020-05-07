from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visitors = Visit.objects.filter(leaved_at=None)
    for visitor in visitors:
        duration = Visit.get_duration(visitor)
        data = {
            'who_entered': visitor.passcard,
            'entered_at': visitor.entered_at,
            'duration': Visit.format_duration(duration),
            'is_strange': Visit.is_visit_long(visitor)
        }
        non_closed_visits.append(data)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
