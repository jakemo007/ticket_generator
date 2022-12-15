from django.shortcuts import  render, redirect
from .forms import NewUserForm, TicketEditForm, TicketForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tickets
from django.urls import reverse_lazy
from django.db.models import F, Value


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
    def form_valid(self, form):
        # form.instance.owner = self.request.user
        # ry :
		# 	print(form.instance)t
        try :
            if self.request.user.is_superuser :
                # print(form.instance.is_deleted)
                form.instance.is_updated = True 
                form.instance.is_updated_by_admin = True
            else : 
                form.instance.is_updated = False 
                form.instance.is_updated_by_admin = True
        except Exception as e:
            print('Exception OCcured', e)
        return super().form_valid(form)

class DeleteTicketView(DeleteView):
    model = Tickets
    template_name = 'delete_ticket.html'
    success_url = reverse_lazy('main:homepage')
	
    # def form_valid(self, form) :
    #     # print(form.instance.author_id)
    #     if self.request.user.is_superuser and not form.instance.is_deleted :
    #         print('Inside delete super user')
    #         form.instance.is_deleted = True 
    #         form.instance.is_updated_by_admin = True
    #         form.save()
    #     elif form.instance.is_deleted :
    #         return super().form_valid(form)
    #     else :
    #         return  super().form_valid(form)


		# model  = Tickets.objects.all()


class NewTicket(CreateView):
    model = Tickets
    form_class = TicketForm
    template_name = 'add_ticket.html'