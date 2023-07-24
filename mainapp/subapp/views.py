from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def fashion(request):
    return render(request, "fashion.html")


def fashion_1(request):
    return render(request, "fashion_1.html")


def fashion_2(request):
    return render(request, "fashion_2.html")


def fashion_3(request):
    return render(request, "fashion_3.html")


def food(request):
    return render(request, "food.html")


def food_1(request):
    return render(request, "food_1.html")


def food_2(request):
    return render(request, "food_2.html")


def transportation(request):
    return render(request, "transportation.html")


def transportation_1(request):
    return render(request, "transportation_1.html")


def transportation_2(request):
    return render(request, "transportation_2.html")


def beauty(request):
    return render(request, "beauty.html")


def beauty_1(request):
    return render(request, "beauty_1.html")


def beauty_2(request):
    return render(request, "beauty_2.html")


def beauty_3(request):
    return render(request, "beauty_3.html")
