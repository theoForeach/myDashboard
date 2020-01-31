from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

import redis

from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'redishboard.html', {})


def get_data(request, *args, **kwargs):
    r = redis.Redis()
    data = {
        "prices_keys": len(r.keys()),
        "hotels": 1
    }
    return JsonResponse(data)  #http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        r = redis.Redis()
        prices_keys = len(r.keys())
        labels = ['Prices', 'Demand', 'Pickup', 'Green', 'Purple', 'Orange']
        default_items = [prices_keys, 1235, 2152, 1516, 1545, 20]
        data = {
            labels: labels,
            "default": default_items,
        }
        return Response(data)

class IndexView(generic.ListView):
    template_name = 'redishboard/index.html'
    context_object_name = 'redis_key_list'

    def get_queryset(self):
        """
        Return all redis keys
        """
        r = redis.Redis()
        # for i in range(1, 10):
        #     r.set('sr_prices_670_2019-12-0{}'.format(i), i+10)
        to_ret = [x.decode('utf-8') for x in r.keys()]
        to_ret.sort()
        return to_ret

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Add any other variables to the context here
        ...
        return context


def detail(request, key):
    r = redis.Redis()
    value = r.get(key)
    return HttpResponse(value if value else 'The key is empty.')


def delete(request, key):
    r = redis.Redis()
    r.delete(key)
    return HttpResponseRedirect(reverse('redishboard:index'))
