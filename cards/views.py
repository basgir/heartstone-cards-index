from django.shortcuts import render
from django.http import HttpResponse
from .models import Card, Deck
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the cards index.")

def all_cards(request):
    """ All trainings view """

    cards = Card.objects.all()
    template = loader.get_template('cards/list.html')
    context = {
            'cards' : cards,
            'base_url' : '../..'
            }
    return HttpResponse(template.render(context, request))

def get_card(request, id):
    """ All trainings view """

    card = Card.objects.get(pk = id)
    template = loader.get_template('cards/single.html')
    context = {
            'card' : card,
            'base_url' : '../..'
            }
    return HttpResponse(template.render(context, request))