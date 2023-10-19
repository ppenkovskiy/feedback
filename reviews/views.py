from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html', {
            'form': form
        })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Great work!'
        return context


class ReviewsListView(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context


# def review_detail(request, slug):
#     identified_review = get_object_or_404(Review, slug=slug)
#     return render(request, 'reviews/review_detail.html',
#                   {'review': identified_review,
#                    })

class ReviewDetailView(TemplateView):
    template_name = 'reviews/review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs.get('id')
        selected_review = Review.objects.get(id=review_id)
        context['review'] = selected_review
        return context