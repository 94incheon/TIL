from django.shortcuts import render
import random

# Create your views here.
def dinner(request, menu, num):
    # menu_list = ['chicken', 'pizza', 'hamburger']
    # menu = random.choice(menu_list)
    context = {
        'menu': menu,
        'num': num
    }

    return render(request, 'dinner.html', context)
