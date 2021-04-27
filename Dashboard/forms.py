from django import forms
import datetime
from Gdriveapi.models import Product

class dashboardForm(forms.Form):

    CHOICES = [('date', 'Date'), ('chal', 'Chal'), ('dal', 'Dal'), ('salt', 'Salt'),
               ('oil', 'Oil'), ('honey', 'Honey'), ('butter', 'Butter'), ('milk', 'Milk'), ]
    CHOICES1 = [ ('chal', 'Chal'), ('dal', 'Dal'), ('salt', 'Salt'),
               ('oil', 'Oil'), ('honey', 'Honey'), ('butter', 'Butter'), ('milk', 'Milk'), ]
    chartchoice = [('line', 'Line'), ('bar', 'Bar')]
    # , ('pie', 'Pie'),('scatter', 'Scatter'), ('polarArea', 'PolarArea'), ('radar', 'Radar'), ('doughnut', 'Doughnut')

    # CHOICES1 = [('1', 'First'), ('2', 'Second')]
    d=Product.objects.values('date').latest('date')
    e=Product.objects.values('date').earliest('date')

    # Date_f = forms.DateField(label='From', widget=forms.SelectDateWidget(
    #     years=range(1950, 2022)), initial=datetime.datetime(2020, 1, 1,), required=False)
    # Date_t = forms.DateField(label='To', widget=forms.SelectDateWidget(
    #     years=range(2020, 2030)), initial=datetime.datetime.now(), required=False)

    Date_f = forms.DateField(label='From', widget=forms.SelectDateWidget(
        years=range(1950, 2022)), initial=e['date'], required=False)
    Date_t = forms.DateField(label='To', widget=forms.SelectDateWidget(
        years=range(2020, 2030)), initial=d['date'], required=False)
    product = forms.CharField(
        label='X-Axis', widget=forms.Select(choices=CHOICES), required=False)
    product1 = forms.CharField(
        label='Y-Axis', widget=forms.Select(choices=CHOICES1), required=False)
    # condition = forms.BooleanField(label='Y-Axis(Multiple Select)',required=False)
    # product2 = forms.MultipleChoiceField(
    #     label='Y-Axis(Multiple Select)', choices=CHOICES, required=False)
    # # product2 = forms.MultipleChoiceField(
    # #     label='Y-Axis(Multiple Select)',widget=forms.SelectMultiple, choices=CHOICES, required=False)

    charttype = forms.CharField(label='Chart Type', widget=forms.Select(
        choices=chartchoice), required=False)
    charttitle = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Char Title'}), required=False)
    # favorite_colors = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple, choices=CHOICES, required=False)
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False)
