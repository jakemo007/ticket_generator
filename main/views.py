from django.shortcuts import  render, redirect
from .forms import NewUserForm, TicketEditForm, TicketForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tickets
from django.urls import reverse_lazy

# def home(request):
#     return render(request=request, template_name="header.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")


class HomeView(ListView):
    model = Tickets
    template_name = 'header.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class TicketDetailView(DetailView):
    model = Tickets
    template_name = 'ticket_view.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Tickets.objects.all()
        context = super(TicketDetailView,self).get_context_data(*args, **kwargs)
        context['ticket'] = cat_menu
        return context

class EditTicketView(UpdateView):
    model = Tickets
    form_class = TicketEditForm
    # fields = ['title','body']
    template_name = 'update_ticket.html'

class DeleteTicketView(DeleteView):
    model = Tickets
    template_name = 'delete_ticket.html'
    success_url = reverse_lazy('main:homepage')

class NewTicket(CreateView):
    model = Tickets
    form_class = TicketForm
    template_name = 'add_ticket.html'