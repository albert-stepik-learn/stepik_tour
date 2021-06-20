from django.shortcuts import render


def main_view(request):
    return render(request, "index.html")


def departure_view(request, departure):
    context = {"departure": departure}
    return render(request, "departure.html", context=context)


def tour_view(request, id):
    context = {'id': id}
    return render(request, 'tour.html', context=context)
