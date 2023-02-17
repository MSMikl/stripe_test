from urllib.parse import urljoin

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse

import stripe
import uuid

from .models import Item

class BuyView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        session = stripe.checkout.Session.create(
            api_key=settings.STRIPE_SECRET_KEY,
            idempotency_key=uuid.uuid4().__str__(),
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price*100),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=urljoin(request.site.domain, reverse('success')),
            cancel_url=urljoin(request.site.domain, reverse('cancel')),            
        )
        return JsonResponse({'session_id': session.stripe_id})
    

class ItemView(TemplateView):

    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        item = get_object_or_404(Item, id=kwargs['item_id'])
        context = {
            'item': item,
            'buy_url': urljoin(self.request.site.domain, reverse('buy', kwargs={'item_id': item.id})),
            'public_key': settings.STRIPE_PUBLIC_KEY,
        }
        return context
    

class ResultView(View):

    result = ''

    def get(self, request):
        return render(request, 'result.html', {'result': self.result})
