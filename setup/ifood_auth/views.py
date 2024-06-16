from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from urllib.parse import urlencode
from .models import AccessToken
import os
from dotenv import load_dotenv

load_dotenv()

def request_token(request):
    if request.method == 'POST':
        url = os.getenv('url')
        client_id = os.getenv('client_id')
        client_secret = os.getenv('client_secret')


        payload = {
            'clientId': client_id,
            'clientSecret': client_secret,
            'grantType': 'client_credentials',
            'merchantApiHost': 'https://merchant-api.ifood.com.br'
        }

        encoded_payload = urlencode(payload)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, data=encoded_payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            access_token = data.get('accessToken')
            token_type = data.get('type')
            expires_in = data.get('expiresIn')

            # Salvar os dados no banco de dados
            access_token_obj = AccessToken.objects.create(access_token=access_token, token_type=token_type, expires_in=expires_in)

            # Redirecionar para a página inicial (change_list)
            return HttpResponseRedirect(reverse('admin:ifood_auth_accesstoken_changelist'))

        else:
            return HttpResponse(f'Failed to obtain access token. Status code: {response.status_code}')

    else:
        return render(request, 'ifood_auth/request_token.html')