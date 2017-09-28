# Create your views here.
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.db import IntegrityError


from .models import Nameaddress
from .forms import NameaddressForm

#define session storage to be used
sess = Session.objects.get(pk='1ex5mx0v1htbx886r7o1ol2au2fmx5na').get_decoded()
sess['msg_message']=''

#'/' index view
def index(request):
    return render(request, 'myapp/index.html')
#'/list' list view
def list(request): 
    if sess['msg_message'] == '':
       name_list = Nameaddress.objects.order_by('name_text')
       context = {'name_list': name_list}
       return render(request, 'myapp/list.html', context)
    else:
       name_list = Nameaddress.objects.order_by('name_text')
       context = {'name_list': name_list, 'msg_message': sess['msg_message']}
       sess['msg_message']=''
       return render(request, 'myapp/list.html', context) 

#'/add/' add contact view
def add(request, data=''):
   if  request.method == 'POST':
       data= request.POST['name_id']
       name_list = Nameaddress.objects.get(pk=data)
       form = NameaddressForm(initial={'name_text': name_list.name_text, 
              'email_text':name_list.email_text})
       return render(request, 'myapp/add.html', {'form': form, 'name_id':data})
   else: 
       form = NameaddressForm()
       return render(request, 'myapp/add.html', {'form': form})

# Save/Edit contact in in the DB, save view
def save(request):
    # if this is a POST request we need to process the form data
    if  request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameaddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if not request.POST['name_id']=="":
              obj = get_object_or_404(Nameaddress, pk=request.POST['name_id']) #get object to be edited
              obj.name_text = request.POST['name_text']
              obj.email_text = request.POST['email_text']
              sess['msg_message']= 'Record edited successfully'
            else:
              obj = Nameaddress() #gets new object
              obj.name_text = form.cleaned_data['name_text'] 
              obj.email_text = form.cleaned_data['email_text'] 
              sess['msg_message']= 'Record saved successfully'
              

            try:
              #finally save the object in db         
              obj.save()
              # redirect to a new URL:  
              return HttpResponseRedirect(reverse('myapp:list'))
            except IntegrityError as e:
              form = NameaddressForm(request.POST)
              return render(request, 'myapp/add.html', {'form': form, 'msg_message':
              'Error: Email address already exists.', 'name_id': request.POST['name_id']})
              
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameaddressForm()
        return render(request, 'myapp/add.html', {'form': form})


#delete record from contact list view
def delete(request, data=''):
   #+some code to check if New belongs to logged in user
   data = request.POST['name_id'];
   obj = Nameaddress.objects.get(pk=data).delete()
   name_list = Nameaddress.objects.order_by('name_text')
   sess['msg_message']='Record deleted Successfully'
   context = {'name_list': name_list, 'msg_message': sess['msg_message']}
   sess['msg_message']=''
   return render(request, 'myapp/list.html', context) 

   
