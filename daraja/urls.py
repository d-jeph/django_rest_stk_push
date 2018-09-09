from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('generate_token/',views.GenerateAccessToken, name = 'generate_token' ),
    #path('validation/', csrf_exempt(views.ValidationView.as_view()), name='major'),
    path('pay/', csrf_exempt(views.MakePayment), name='pay'),
    path('confirmation/', csrf_exempt(views.CofirmPayment), name='confirm_payment'),
]