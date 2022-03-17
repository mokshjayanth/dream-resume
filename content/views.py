from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.http import FileResponse, Http404, HttpResponse
from django.urls import reverse
from .models import *
from .forms import *
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupView(CreateView):
    template_name = "registration/signup.html"
   
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

'''
#This is Function based views which is equivalent to Index(ListView).

def index(request):
    edu_query_set = Education.objects.all()
    pro_query_set = Project.objects.all()
    skill_query_set = Skill.objects.all()
    context = {
        'education': edu_query_set,
        'projects' : pro_query_set,
        'skills': skill_query_set
    }
    return render(request,'index.html', context)

'''

class Index(LoginRequiredMixin,ListView):
    template_name = "index.html"
    context_object_name = "skills"
    queryset = Skill.objects.all()

    def get_context_data(self, **kwargs):
        user = self.request.user
        qs1 = Education.objects.all().filter(user_profile =user.userprofile)
        qs2 = Skill.objects.all().filter(user_profile =user.userprofile)
        qs3 = Project.objects.all().filter(user_profile =user.userprofile)
        context = super().get_context_data(**kwargs)
        context['education'] = qs1
        context['skills'] = qs2
        context['projects'] = qs3
        return context
    

class DetailedEdu(DetailView):
    template_name = "content/detail_edu.html"
    queryset = Education.objects.all()
    context_object_name = "record"

class DetailedPro(DetailView):
    template_name = "content/detail_pro.html"
    queryset = Project.objects.all()
    context_object_name = "record"

class DetailedSkill(DetailView):
    template_name = "content/detail_skill.html"
    queryset = Skill.objects.all()
    context_object_name = "record"

class UpdateEdu(LoginRequiredMixin, UpdateView):
    template_name = "content/edu_form.html"
    queryset = Education.objects.all()
    form_class = EduForm

    def get_success_url(self):
        return "/"

class UpdateSkill(LoginRequiredMixin, UpdateView):
    template_name = "content/skill_form.html"
    queryset = Skill.objects.all()
    form_class = SkillForm

    def get_success_url(self):
        return "/"

class UpdatePro(LoginRequiredMixin, UpdateView):
    template_name = "content/pro_form.html"
    queryset = Project.objects.all()
    form_class = ProForm

    def get_success_url(self):
        return "/"

'''
# These are Function-Based Views.

def addEdu(request):
    form = EduForm()
    if request.method == "POST":
        form = EduForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/")
    context = {
        'form': form
    }
    return render(request,'content/edu_form.html',context)

    def addPro(request):
    form = ProForm()
    if request.method == "POST":
        form = ProForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        'form': form
    }
    return render(request,'content/pro_form.html',context)

def addSkill(request):
    print("OUT")
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect("/")
    else:
        form = SkillForm()  
    context = {
        'form': form
    }
    return render(request,'content/skill_form.html',context)
'''

class AddEdu(LoginRequiredMixin, CreateView):
    template_name = "content/edu_form.html"
    model = Education
    form_class = EduForm

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        education = form.save(commit=False)
        education.user_profile = self.request.user.userprofile
        education.save()
        return super().form_valid(form)

class AddPro(LoginRequiredMixin, CreateView):
    template_name = "content/pro_form.html"
    model = Project
    form_class = ProForm

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        project = form.save(commit=False)
        project.user_profile = self.request.user.userprofile
        project.save()
        return super().form_valid(form)

class AddSkill(LoginRequiredMixin, CreateView):
    template_name = "content/skill_form.html"
    model = Skill
    form_class = SkillForm

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        skill = form.save(commit=False)
        skill.user_profile = self.request.user.userprofile
        skill.save()
        return super().form_valid(form)

class DeleteEdu(LoginRequiredMixin, DeleteView):
    template_name = "content/delete.html"
    queryset = Education.objects.all()
    def get_success_url(self):
        return "/"

class DeleteSkill(LoginRequiredMixin, DeleteView):
    template_name = "content/delete.html"
    queryset = Skill.objects.all()
    def get_success_url(self):
        return "/"

class DeletePro(LoginRequiredMixin, DeleteView):
    template_name = "content/delete.html"
    queryset = Project.objects.all()
    def get_success_url(self):
        return "/"


 
def pdf_view(request,pk):
    try:
        skill = Skill.objects.get(id=pk)
        #return(FileResponse(open(skill.certificate.url, 'rb'), content_type='application/pdf', as_attachment=False))
        return redirect(skill.certificate.url)
    except FileNotFoundError:
        raise Http404()