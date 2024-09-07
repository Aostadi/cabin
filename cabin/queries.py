from django.db.models import Sum, Count, Q, IntegerField
from django.db.models.functions import Coalesce

from .models import *


def query_0(x):
    q = Driver.objects.filter(rating__gt=x)
    return q


def query_1():
    q = Payment.objects.aggregate(income=Coalesce(Sum('amount', output_field=IntegerField()), 0))
    print(q)
    return q


def query_2(x):
    q = (
        Payment.objects.filter(ride__request__rider=x).aggregate(
            payment_sum=Coalesce(Sum('amount', output_field=IntegerField()), 0)
        )
    )
    return q


def query_3():
    q = Driver.objects.filter(car__car_type='A').distinct().count()
    return q


def query_4():
    q = RideRequest.objects.filter(rider__isnull=True)
    return q


def query_5(t):
    q = Rider.objects.annotate(total_peyment=Sum("riderequest__ride__payment__amount").filter(total_peyment__gte=t))
    return q


def query_6():
    q = Account.objects.filter(drivers__isnull=False).annotate(num_cars=Count('drivers__car')).order_by('-num_cars',
                                                                                              'last_name').first()
    return q


def query_7():
    q = Rider.objects.filter(riderequest__ride__car__car_type="A").annotate(
        n=Count(
            'riderequet__ride',
            filter=Q(riderequest__ride__car__car_type="A")
        )
    )
    return q


def query_8(x):
    q = Driver.objects.filter(car__model__gte=x).values('account__email').distinct()
    return q


def query_9():
    q = Driver.objects.annotate(n=Count('car__ride'))
    return q


def query_10():
    q = Driver.objects.filter(account__driver__isnull=False).values('account__name').annotate(
        n=Count('account__drivers__ride')
    )
    return q


def query_11(n, c):
    q = Driver.objects.filter(car__color=c, car__model=n).distinct()
    return q


def query_12(n, c):
    q1 = Driver.objects.filter(car__model__gte=n).distinct()
    q2 = Driver.objects.filter(car__color=c).distinct()
    q = q1.intersection(q2)
    return q


def query_13(n, m):
    q = Ride.objects.filter(car__owner__account__first_name=n,
                            request__rider__account__first_name=m).aggregate(
        sum_duration=Sum('dropoff_time') - Sum('pickup_time'))
    return q


def query_14(x, y, r):
    q = 'your query here'
    return q


def query_15(n, c):
    q = 'your query here'
    return q


def query_16(x, t):
    q = 'your query here'
    return q


def query_17():
    q = 'your query here'
    return q


def query_18():
    q = 'your query here'
    return q


def query_19(n, t):
    q = 'your query here'
    return q


def query_20():
    q = 'your query here'
    return q
