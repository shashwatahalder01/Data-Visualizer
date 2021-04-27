from django.shortcuts import redirect, render
from json import dumps
from Gdriveapi.models import Product
import datetime
from .forms import dashboardForm


# Create your views here.
def dashboard(requests):
    user = requests.user
    if user.is_authenticated:
        form = dashboardForm(requests.POST or None)
        if requests.method == 'POST':
            if form.is_valid():
                # requests.session.set_expiry(5)
                # print('session_id_or_key:')
                # print(requests.session.session_key)
                # print('session_expire_date:')
                # print(requests.session.get_expiry_date())

                Date_f = form.cleaned_data.get("Date_f")
                Date_t = form.cleaned_data.get("Date_t")
                xaxis = form.cleaned_data.get("product")
                yaxis = form.cleaned_data.get("product1")
                charttype = form.cleaned_data.get("charttype")
                charttitle = form.cleaned_data.get("charttitle")

                #########

                """
                    yaxis_multi=form.cleaned_data.get("product2")
                    condition =str(form.cleaned_data.get("condition")).lower()
                    """

                # print(condition)
                # condition =form.cleaned_data.get("condition").lower()
                # print(condition)
                # favorite_colors=form.cleaned_data.get("favorite_colors")
                # choice_field=form.cleaned_data.get("choice_field")
                # print(Date_f)
                # print(Date_t)
                # print(xaxis)
                # print(yaxis)
                # print(charttype)
                # print(charttitle)
                # print(favorite_colors)
                # print(choice_field)

                if not charttitle:
                    charttitle = 'Your Chart Title'

                # yaxis_multi = list(yaxis_multi.split(","))

                ##########
                """
                    yaxis_multidatalist=[]
                    u=[]
                    if  yaxis_multi:
                        for val in yaxis_multi:
                            val2=Product.objects.values_list(val)
                            for it in val2:
                                u = u+list(it)
                            yaxis_multidatalist.append(u)
                    # print(len(yaxis_multidatalist))
                    z=[]
                    for q in range(len(yaxis_multidatalist)):
                            p = {
                                'label': yaxis_multi[q],
                                'data': yaxis_multidatalist[q],
                                'fill': 'false',
                                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                                'borderColor': 'rgba(255, 99, 132, 1)',
                                'borderWidth': 1,
                            }
                            z.append(p) 
                    """

                # print(len(z))

                # value from date range

                # start_date = datetime.date(2020, 1, 1)
                # end_date = datetime.date(2020, 2, 28)
                # c=Product.objeacts.values_list('date').filter(date__range=(start_date, end_date))
                # c=Product.objects.dates('date', 'year')

                l, m, n, x, y = [], [], [], [], []
                a = Product.objects.values_list(xaxis)
                b = Product.objects.values_list(yaxis)
                c = Product.objects.values_list('date').filter(date__range=(Date_f, Date_t))
                # d=Product.objects.values('date').latest('date')
                # e=Product.objects.values('date').earliest('date')
                # print(d['date'])
                # print(e['date'])

                # x axix date or not

                # if yaxis!= 'date':
                if xaxis != 'date':
                    for item in a:
                        m = m+list(item)
                    x = m
                else:
                    for item in c:
                        # item=item[0].strftime("%B")
                        item = item[0].strftime("%Y-%m-%d")
                        # l = l+list(it)
                        l.append(item)
                    x = l

                for item in b:
                    n = n+list(item)
                # y=n
                v = {
                    'label': yaxis,
                    'data': n,
                    'fill': 'false',
                            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                            'borderColor': 'rgba(255, 99, 132, 1)',
                            'borderWidth': 1,
                }
                y.append(v)
                # y axix date or not
                # if xaxis != 'date':
                #     a = Product.objects.values_list(yaxis)
                #     b = Product.objects.values_list(xaxis)
                #     c = Product.objects.values_list('date').filter(date__range=(Date_f, Date_t))
                #     if yaxis != 'date':
                #         for item in a:
                #             m = m+list(item)
                #         y=m
                #     else:
                #         for item in c:
                #             # item=item[0].strftime("%B")
                #             item=item[0].strftime("%Y-%m-%d")
                #             # l = l+list(it)
                #             l.append(item)
                #         y=l

                #     for item in b:
                #         n = n+list(item)
                #     x=n

                chartinfo = {
                    'type': charttype,
                    'title': charttitle,
                    'label': yaxis,
                    'x': x,
                    'y': y,
                    # 'condition':condition,
                    # 'z':z,

                }
                data = dumps(chartinfo)
                # print(data)
                html = {'title': 'Dashboard', 'user': user,
                        'form': form, 'data': data}
                link = 'dashboard/dashboard.html'
                return render(requests, link, html)
            
            else:
                html = {'title': 'Dashboard', 'user': user, 'form': form}
                link = 'dashboard/dashboard.html'
                return render(requests, link, html)
        else:
            html = {'title': 'Dashboard', 'user': user, 'form': form}
            link = 'dashboard/dashboard.html'
            return render(requests, link, html)
    else:
        return redirect('/')


# import datetime

# x = datetime.date(2021, 12, 31)

# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.strftime("%Y"))
# print(x.strftime("%B"))
# print(x.strftime("%A"))
# print(x.strftime("%Y-%m-%d"))
