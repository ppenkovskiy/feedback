from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Great work!'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1)
        return data


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review


class AddFavoriteView(View):
    def post(self, requests):
        review_id = requests.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        requests.session["fav_review"] = fav_review
        return HttpResponseRedirect('/reviews/' + review_id)