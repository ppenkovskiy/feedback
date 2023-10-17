from django.shortcuts import render


def review(request):
    return render(request, 'reviews/review.html', )