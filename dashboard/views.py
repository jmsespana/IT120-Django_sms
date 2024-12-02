from django.shortcuts import render, redirect

# Welcome Page View
def welcome_view(request):
    return render(request, "front_page.html")


# Quiz Page View
def quiz_view(request):
    return render(request, "quiz.html")

