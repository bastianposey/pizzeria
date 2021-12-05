from django.shortcuts import render

# from pizza_place.forms import TopicForm, EntryForm

# from .models import Topic, Entry

def index(request):
    '''The hame page for pizzeria'''
    return render(request, 'pizza_place/index.html')