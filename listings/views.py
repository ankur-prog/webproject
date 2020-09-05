from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, price_choices, state_choices


# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')

    context = {
        'listings': paginator.get_page(page_number)
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-listing_date')

    # search with keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # get the result if description matching keyword
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # search with City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # get the result if description matching keyword
            queryset_list = queryset_list.filter(city__iexact=city)

    # search with state
    if 'state' in request.GET:
        state = request.GET['state']

        if state and state!='State (All)':
            # get the result if description matching keyword
            queryset_list = queryset_list.filter(state__iexact=state)
    # search with bedrooms
    if 'bedrooms' in request.GET:
        bedroom = request.GET['bedrooms']
        print(bedroom)
        if bedroom and bedroom!='Bedrooms (All)':
            # get the result if description matching keyword
            queryset_list = queryset_list.filter(bedroom__lte=bedroom)
    # search with prices
    if 'price' in request.GET:
        price = request.GET['price']
        if price and price!='Max Price (Any)':
            # get the result if description matching keyword
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
