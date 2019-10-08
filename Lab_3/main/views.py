from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime



def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    date_now = datetime.now()
    date = date_now.strftime("%Y-%m-%d %H:%M:%S")
    page = request.path
    os_info = os.uname()
    client = request.META['HTTP_USER_AGENT']
    response = {'date': date,
                'current_page': page,
                'server_info': {
                 'System': os_info.sysname,
                 'Release': os_info.release,
                 'Type': os_info.machine,
                },
                'client_info': client}
    return JsonResponse(response)