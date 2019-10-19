"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render 
from subprocess import run,PIPE 
import sys
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app import routerssh
from django import forms

def home(request):

    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(required=False, label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'app/contact.html', {'form': form, 'submitted': submitted})
#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        }
#    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def work(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/work.html',
        {
            'title':'work',
            'message':'Here we will implement the App',
            'year':datetime.now().year,
        }
    )

def button(request):
    return render(request, 'work.html')

def sshrouter(request):
    response = HttpResponse(alarm, content_type='text/plain')
    response_a = sshrouter(response)
    return response_a

#def external(request):
#    inp= request.POST.get('param')
#    out= run([sys.executable,'E:\Programming-test\DjangoWeb\DjangoWeb\app\router-ssh.py'],shell=False,stdout=PIPE)
#    print(out)
#    return render(request,'app\work.html',{'data1':out.stdout})
#    #return render(request,'app\work.html',{'data1':out})
