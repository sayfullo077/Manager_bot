from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View, TemplateView
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import timedelta
from .forms import EmployeeForm, TaskForm, CompanyInfoForm, CompanyStructureForm
from .models import Task, Employee, TelegramUser, Advance, CompanyInfo, CompanyStructure, Offer, Complaint  

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        employees = Employee.objects.count()
        tasks = Task.objects.count()
        advances = Advance.objects.count()
        today_advances = Advance.objects.filter(add_date__date=today)
        today_tasks = Task.objects.filter(add_date__date=today)
        today_employee = Employee.objects.filter(add_date__date=today)
        all_tasks = today_tasks.count()
        all_employee = today_employee.count()
        all_advances = today_advances.count()
        
        context['tasks'] = tasks
        context['advances'] = advances
        context['all_tasks'] = all_tasks
        context['all_advances'] = all_advances
        context['employees'] = employees
        context['today_tasks'] = today_tasks
        context['all_employee'] = all_employee
        return context

class AddTaskView(LoginRequiredMixin, View):
    def get(self, request):
        xodimlar = Employee.objects.all()
        return render(request, 'add_task.html', {"xodimlar": xodimlar})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            
            selected_employees_ids = request.POST.getlist('employees')
            task.employees.set(selected_employees_ids)

            return redirect('main:task')
        return render(request, 'add_task.html', {'form': form})
    
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('main:task')

    def form_valid(self, form):
        return super(TaskUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(TaskUpdateView, self).form_invalid(form)
    
class CompanyInfoView(View):
    model = CompanyInfo
    form_class = CompanyInfoForm
    template_name = 'company_info.html'
    success_url = reverse_lazy('main:company_info')
    
    def get(self, request):
        form = CompanyInfoForm()
        latest_company_info = CompanyInfo.objects.latest('add_date')
        return render(request, 'company_info.html', {'form': form, 'latest_company_info': latest_company_info})

class CompanyInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyInfo
    form_class = CompanyInfoForm
    template_name = 'add_info.html'
    success_url = reverse_lazy('main:company_info')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class CompanyStructureView(LoginRequiredMixin, View):
    model = CompanyStructure
    form_class = CompanyStructureForm
    template_name = 'company_structure.html'
    success_url = reverse_lazy('main:company_structure')
    
    def get(self, request):
        form = CompanyInfoForm()
        latest_company_info = CompanyStructure.objects.latest('add_date')
        return render(request, 'company_structure.html', {'form': form, 'latest_company_info': latest_company_info})
    
class CompanyStructureUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyStructure
    form_class = CompanyStructureForm
    template_name = 'update_company_structure.html'
    success_url = reverse_lazy('main:company_structure')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class TaskDetailView(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, 'task_detail.html', {'task': task})
    
class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()            
        context['tasks'] = tasks
        return context
 
class DeleteTaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('/task')
    
class AddEmployeeView(LoginRequiredMixin, View):
    template_name = 'add_employee.html'
    form_class = EmployeeForm

    def get(self, request):
        form = self.form_class()
        users = TelegramUser.objects.all() 
        return render(request, self.template_name, {'form': form, 'users': users})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:employee')
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})
    
class EmployeeView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Employee.objects.all()            
        context['employees'] = employees
        return context
    
class UpdateEmployeeView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'update_employee.html'
    success_url = reverse_lazy('main:employee')

    def form_valid(self, form):
        return super(UpdateEmployeeView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UpdateEmployeeView, self).form_invalid(form)

class DeleteEmployeeView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect('/employee')
    
class AdvanceView(LoginRequiredMixin, ListView):
    model = Advance
    template_name = 'advance.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advance = Advance.objects.all()            
        context['advance'] = advance
        return context 
    
class DeleteAdvanceView(LoginRequiredMixin, View):
    def get(self, request, pk):
        advance = get_object_or_404(Advance, pk=pk)
        advance.delete()
        return redirect('/advance')
    
    
class OfferView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'offer.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offers = Offer.objects.all()            
        context['offers'] = offers
        return context
    
class DeleteOfferView(LoginRequiredMixin, View):
    def get(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        offer.delete()
        return redirect('/offer')

class ComplaintView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = 'complaint.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complaint = Complaint.objects.all()            
        context['complaint'] = complaint
        return context
    
class DeleteComplaintView(LoginRequiredMixin, View):
    def get(self, request, pk):
        complaint = get_object_or_404(Complaint, pk=pk)
        complaint.delete()
        return redirect('/complaint')
    
class AdminsView(LoginRequiredMixin, View):
    template_name = 'admins.html'

    def get(self, request):
        user = User.objects.all()[1:]
        return render(request, self.template_name, {'user': user})

class DeleteAdminsView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('/admins')
    
def login_view(request):
    form = AuthenticationForm()
    context = {"form": form}

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main:home")

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect('main:login')

def register_view(request):
    form = UserCreationForm()
    context = {"form": form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            login(request, user)
            
            messages.success(request, "Foydalanuvchi ro'yxatdan o'tdi !")
            return redirect("main:login")
        else:
            messages.error(request, "Foydalanuvchi ro'yxatdan o'tmadi !")

    return render(request, "register.html", context)
        
def search(request):
    query = request.GET.get('q')

    if query:
        results = []

        telegram_users1 = TelegramUser.objects.filter(full_name__icontains=query)
        employees = Employee.objects.filter(full_name__icontains=query)
        telegram_users = TelegramUser.objects.filter(telegram_id__icontains=query)
        employees_telegram_id = Employee.objects.filter(telegram_id__in=telegram_users, full_name__icontains=query)
        tasks = Task.objects.filter(name__icontains=query)
        advances = Advance.objects.filter(desc__icontains=query)
        company_infos = CompanyInfo.objects.filter(text__icontains=query)
        company_structures = CompanyStructure.objects.filter(text__icontains=query)

        # Adding querysets to results list
        results.extend(telegram_users1)
        results.extend(telegram_users)
        results.extend(employees)
        results.extend(employees_telegram_id)
        results.extend(tasks)
        results.extend(advances)
        results.extend(company_infos)
        results.extend(company_structures)

    else:
        results = None

    context = {
        'results': results,
        'query': query
    }
    return render(request, 'search_results.html', context)

