# Hearthstone-cards-index
Simple project started in the HSG summer coding bootcamp.

The project consists of a basic Django web-app which shows cards and decks
which are stored in the database.

## Routes
The app provides the following routes 

/cards : shows all cards

/cards/1 : shows the index 1 card

/admin : access to the django admin panel

/ : shows the index route


# Models
There exist two different models at the moment:

Cards : name, img_url, health, attack, etc...

Deck : Cards


# Installation

```bash
$ pip3 install Django 
```

# How to run

```bash
$ python3 manage.py runserver
```



