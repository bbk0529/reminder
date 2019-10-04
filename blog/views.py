from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import json



def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘','내일', 'Exchange']
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘':
        today = "오늘 급식"

        return JsonResponse({
                'message': {
                    'text': today
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘','내일', 'Exchange']
                }

            })

    elif datacontent == '내일':
        tomorrow = "내일 급식"

        return JsonResponse({
                'message': {
                    'text': tomorrow
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘','내일', 'Exchange']
                }

            })

    elif datacontent =='Exchange':
        link="https://www.google.de/search?q=1euro+to+krw&oq=1euro+to+krw"
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
                    'buttons':['오늘','내일', 'Exchange']
                }

            })
