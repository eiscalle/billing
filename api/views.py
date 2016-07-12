from django.http import Http404
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView, ListAPIView

from api.models import BillingUser, Order
from api.serializers import BillingUserSerializer, OrderSerializer
from api.twocheckout import authorize


class BillingUserView(RetrieveAPIView):
    serializer_class = BillingUserSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'
    queryset = BillingUser.objects.all()

    def get_object(self):
        obj = self.queryset.filter(user_id=self.kwargs['user_id'])
        if not obj.exists():
            obj = BillingUser()
            obj.user_id = self.kwargs['user_id']
            obj.save()
        else:
            obj = obj.get()
        return obj


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        qs = super(OrderListView, self).get_queryset()
        qs = qs.filter(user__user_id=self.kwargs['user_id'])
        qwe = authorize()
        return qs


class Home(ListView):
    model = Order
    template_name = 'home.html'

    def get_queryset(self):
        qs = super(Home, self).get_queryset()
        qs = qs.filter(user__user_id=self.kwargs['user_id'])
        return qs

    def get(self, request, *args, **kwargs):
        user = BillingUser.objects.filter(user_id=self.kwargs['user_id'])
        if not user.exists():
            raise Http404
        self.user = user.get()
        return super(Home, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['billing_user'] = self.user
        return context