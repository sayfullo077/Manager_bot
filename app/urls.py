from django.urls import path
from .views import CompanyStructureUpdateView, CompanyStructureView, CompanyInfoUpdateView, CompanyInfoView, DeleteComplaintView, ComplaintView, OfferView, DeleteOfferView, DeleteAdminsView, AdminsView, search, HomeView, DeleteAdvanceView, EmployeeView, AddEmployeeView, UpdateEmployeeView, DeleteEmployeeView, TaskView, DeleteTaskView, TaskDetailView, AddTaskView, TaskUpdateView, AdvanceView, login_view, logout_view , register_view
app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("company_info/", CompanyInfoView.as_view(), name='company_info'),
    path("company_structure/", CompanyStructureView.as_view(), name='company_structure'),
    path("employee/", EmployeeView.as_view(), name='employee'),
    path("add_employee/", AddEmployeeView.as_view(), name='add_employee'),  
    path("delete_employee/<int:pk>/delete", DeleteEmployeeView.as_view(), name='delete_employee'),
    path("task/", TaskView.as_view(), name='task'),
    path('delete_task/<int:pk>/delete', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name='task'),
    path("add_task/", AddTaskView.as_view(), name='add_task'),
    path('update_task/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('update_employee/<int:pk>/', UpdateEmployeeView.as_view(), name='update_employee'),
    path('company_info/update/<int:pk>/', CompanyInfoUpdateView.as_view(), name='update_company_info'),
    path('update_company_structure/update/<int:pk>/', CompanyStructureUpdateView.as_view(), name='update_company_structure'),
    path("advance/", AdvanceView.as_view(), name='advance'),
    path("complaint/", ComplaintView.as_view(), name='complaint'),
    path("offer/", OfferView.as_view(), name='offer'),
    path('delete_advance/<int:pk>/delete', DeleteAdvanceView.as_view(), name='delete_advance'),
    path('delete_offer/<int:pk>/delete', DeleteOfferView.as_view(), name='delete_offer'),
    path('delete_admins/<int:pk>/delete', DeleteAdminsView.as_view(), name='delete_admins'),
    path('delete_complaint/<int:pk>/delete', DeleteComplaintView.as_view(), name='delete_complaint'),
    path('admins/', AdminsView.as_view(), name='admins'),
    path("search/", search, name='search'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view , name='register'),
]