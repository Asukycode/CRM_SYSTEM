from ast import Del
from django.shortcuts import render, redirect, reverse
# from django.http import HttpResponse
from .models import Client, Agent
from .forms import ClientForm, ClientModelForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

# in  programming what we basically do is Called CRUD
# CRUD create retrieve update delete
# so when using the class base view we have different views which are
# templateview , Deleteview , Updateview , createview, listview

class LandingPage(TemplateView):
    template_name = "landing.html"


# def landing_page(request):
#     return render(request, 'landing.html')

class ClientListView(ListView):
    template_name = 'clients/client_list.html'
    queryset = Client.objects.all()
    # to override the context object_name  we use
    context_object_name = 'clients'


# def client_list(request):
#     clients = Client.objects.all()
#     number_of_clients = clients.count()
#
#     context = {
#         "clients": clients,
#         "num_clients": number_of_clients
#     }
#     return render(request, 'clients/client_list.html', context)

# when working with the detail view the code automatically finds the primary key of that data unlike function views
class ClientDetailView(DetailView):
    template_name = 'clients/client_detail.html'
    queryset = Client.objects.all()
    context_object_name = 'client'



# def client_detail(request, pk):
#     client = Client.objects.get(id=pk)
#
#     context = {
#         "client": client,
#     }
#     return render(request, "clients/client_detail.html", context)



class ClientCreateView(CreateView):
    template_name = 'clients/client_creation.html'
    form_class = ClientModelForm
    # since we have to redirect to /clients create a function below 

    def get_success_url(self):
        # return '/clients'
        # instead we can use a reverse function
        return reverse('clients:client-list')

# def client_create(request):
#     form = ClientModelForm()
#     if request.method == "POST":
#         form = ClientModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#         print("client successfully created and added to Cremdell")
#         return redirect('/clients')

#     context = {
#         "form": form,
#     }

#     return render(request, "clients/client_creation.html", context)


# Note when using the model form it already helps to process the cleaned data
# so there is no need for all of this below i.e (cleaned_data format)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
#             Client.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
# all you need to do is to save the form
# so this is the approach below
#
# if form.is_valid():
#    form.save()



class ClientUpdateView(UpdateView):
    template_name = 'clients/client_update.html'
    form_class = ClientModelForm
    queryset = Client.objects.all()
    
    def get_success_url(self) :
        return reverse('clients:client-list')
        
# def client_update(request, pk):
#     client = Client.objects.get(id=pk)
#     form = ClientModelForm(instance=client)

#     if request.method == 'POST':
#         form = ClientModelForm(request.POST, instance=client)
#         if form.is_valid():
#             form.save()
#             print(client.first_name)
#             return redirect('clients:client-detail', client.pk)
#     context = {
#         'client': client,
#         'form': form,

#     }
#     return render(request, 'clients/client_update.html', context)


'''
So here is how this works the client variable is getting the client we 
want to update by the pk of it amd weve stored client form in the variable form

this part
 if request.method == "POST":
        form = ClientForm(request.POST)
         
         it helps to get what the user has inputed and stored it in the form 
         then form is checked whether it is valid 
         
         if it is valid
         then we redelcare this
         first_name = form.cleaned_data['first_name']
         last_name = form.cleaned_data['last_name']
         age = form.cleaned_data['age']
         
         then now we do this
         client.first_name = first_name
         client.last_name = last_name
         client.age = age
         
         then save it with
         client.save()
         
         
         
         
'''

# But if we are using the clientModelForm

'''
def client_update(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientModelForm(instance=client)

    if request.method == 'POST':
        form = ClientModelForm(request.POST, instance= client)
        if form.is_valid():
            form.save()
            print("client successfully updated")
            return redirect("/clients")
    context = {
        'client': client,
        'form': form,

    }
    return render(request, 'clients/client_update.html', context)


'''

class ClientDeleteView(DeleteView):
    template_name = 'clients:client-update  '
    queryset = Client.objects.all()
    def get_success_url(self):
        return reverse('clients:client-list')
# def client_delete(request, pk):
#     client = Client.objects.get(id=pk)
#     client.delete()
#     return redirect('/clients')

l.,