from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
from contacts.models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        realtor_email = request.POST['realtor_email']

        # check if logged in user has already made an enquiry
        # fetch listing id and user id from saved contact
        # if matches show alert message
        if request.user.is_authenticated:
            user_id = request.user.id

            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made and inquiry for this properties ."
                                       " Our team will contact you soon")
                return redirect("/listings/" + listing_id)

        contact_details = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone,
                                  message=message,
                                  user_id=user_id)
        contact_details.save()
        # sent email to broker
        send_mail(
            'Property Listing enquiry',
            'There has been enquiry for ' + listing + ".  Sign in admin panel for more details.",
            'teamankur30@gmail.com',
            [realtor_email],
            fail_silently=False,
        )
        # sent email to logged in user
        if request.user.is_authenticated:
            user_name = request.user.first_name
            user_email = request.user.email
            send_mail(
                'Real State Team',
                'Dear ' + user_name + '\n' + 'Thank you for your interest in property '+listing +
                '. Our team will reach you soon.',
                'teamankur30@gmail.com',
                [user_email],
                fail_silently=False,
                )
        messages.success(request, 'Your request has been submitted successfully. Broker will contact you soon.')
        return redirect("/listings/" + listing_id)
