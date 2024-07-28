from django.shortcuts import render


# Create your views here.
def raspberry_lora(response):
    return render(response, "app_rasp_lora.html", {})



# def raspberry_lora(response):
#     response.user
#     return render(response, "raspberry_lora\templates\app_rasp_lora.html", {})