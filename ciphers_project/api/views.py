from django.shortcuts import JsonResponse

def greetings(request):
    result = {"message": "Welcome to cipher services!"}
    return JsonResponse(result)