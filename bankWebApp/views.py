from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registrationForm
from .models import cust_details
from django.core.urlresolvers import reverse
from django.template import loader, Context
# from django.templatetags.static import static
from django.views import generic
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def display(request):
    # return HttpResponseRedirect("bankWebApp/demo.html")
    t = loader.get_template('bankWebApp/demo.html')
    return HttpResponse(t.render())

def registration(request):
    if request.method == 'POST':

        form = registrationForm(data=request.POST,files=request.FILES)
        # myfile = request.FILES['cust_picture']
        if form.is_valid():
            form.save()
            # cust_account_id =request.POST.get('cust_account_id')
            # cust_name =request.POST.get('cust_name')
            # cust_address =request.POST.get('cust_address')
            # cust_dob =request.POST.get('cust_dob')
            # cust_email =request.POST.get('cust_email')
            # cust_balance =request.POST.get('cust_balance')
            # cust_picture=request.POST.get('cust_picture')
            # print(cust_picture)
            # registrationObj=cust_details(cust_account_id=cust_account_id,cust_name=cust_name,cust_address=cust_address,cust_dob=cust_dob,cust_email=cust_email,cust_balance=cust_balance,cust_picture=cust_picture)
            # registrationObj.save()

            return HttpResponseRedirect(reverse("login"))
        else:
            print(form.errors)
            print("Invalid form")
            # return HttpResponseRedirect(reverse('registration'))
    else:
        form=registrationForm()

    return render(request,"bankWebApp/Form.html", {"form": form})

def login(request):
    t = loader.get_template('bankWebApp/login.html')
    return HttpResponse(t.render())

class DetailView(generic.DetailView):
    model = cust_details
    pk_url_kwarg = 'detail'
    template_name = 'bankWebApp/details.html'


    # /home/monish/WEEK-7[MONISH]/My Banksrcsrc/home/monish/WEEK-7[MONISH]/My Bank/src