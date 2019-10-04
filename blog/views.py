from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import json



def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['Euro','Dollar']
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == 'Euro':
        link="https://www.google.de/search?q=1euro+to+krw&oq=1euro+to+krw"
        page=requests.get(link)
        soup=BeautifulSoup(page.content, 'html.parser')
        result=soup.find(class_="BNeawe iBp4i AP7Wnd").get_text()

        return JsonResponse({
                'message': {
                    'text': result
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['Euro','Dollar']
                }

            })


    elif datacontent =='Dollar':
        link="https://www.google.de/search?q=1dollar+to+krw&oq=1dollar+to+krw"
        page=requests.get(link)
        soup=BeautifulSoup(page.content, 'html.parser')
        result=soup.find(class_="BNeawe iBp4i AP7Wnd").get_text()
        print(result)

        return JsonResponse({
                'message': {
                    'text': result
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['Euro','Dollar']
                }

            })
