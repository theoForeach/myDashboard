from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Connection

import redis


class IndexView(generic.ListView):
    template_name = 'redishboard/index.html'
    context_object_name = 'redis_key_list'

    def get_queryset(self):
        """
        Return all redis keys
        """
        connection = Connection.objects.filter(id=1)
        r = redis.Redis(connection.get().host, connection.get().port, connection.get().db_id)
        for i in range(1, 10):
            r.set('sr_prices_670_2019-12-0{}'.join(i), i+10)
        return [x.decode('utf-8') for x in r.keys()][:2]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['connection_list'] = Connection.objects.all().order_by('id')

        # Add any other variables to the context here
        ...
        return context


def delete(request, key):
    connection = Connection.objects.filter(id=1)
    r = redis.Redis(connection.get().host, connection.get().port, connection.get().db_id)
    r.delete(key)
    return HttpResponseRedirect(reverse('redishboard:index'))
