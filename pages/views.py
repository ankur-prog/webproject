from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing, Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)[:3]

    context = {'listings': listings,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices}
    return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
     # get mvp
    mvps_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {'realtors': realtors,
               'mvp_realtors':mvps_realtors}
    return render(request, 'pages/about.html', context)