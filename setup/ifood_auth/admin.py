from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import AccessToken
from .views import request_token

class AccessTokenAdmin(admin.ModelAdmin):
    change_list_template = "admin/ifood_auth/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('request-token/', self.admin_site.admin_view(self.request_token))
        ]
        return custom_urls + urls

    def request_token(self, request):
        return HttpResponseRedirect("/ifood-auth/request-token/")

admin.site.register(AccessToken, AccessTokenAdmin)
