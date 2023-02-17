from django.urls import path

from .views import BuyView, ItemView, ResultView

urlpatterns = [
    path('buy/<str:item_id>/', BuyView.as_view(), name='buy'),
    path('item/<str:item_id>/', ItemView.as_view(), name='item'),
    path('payment/success/', ResultView.as_view(result='Платеж успешный'), name='success'),
    path('payment/cancel/', ResultView.as_view(result='Платеж отменен'), name='cancel'),
]