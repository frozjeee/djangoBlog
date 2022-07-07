from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseModelForm
# Create your views here.


class CourseView(View):
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context["object"] = obj
            return render(request, 'courses/course-detail.html', context)
        context["object_list"] = Course.objects.all()
        return render(request, 'courses/course-list.html', context)


class CourseCreateView(View):
    template_name = 'courses/course-create.html'

    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = 'courses/course-update.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = CourseModelForm()
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)
# class CourseDetailView(View):
#     def get(self, request, id_=None, *args, **kwargs):
#         obj = Course.objects.id(self.id)
#         context = {
#             "object": obj
#     }
#         return render(request, 'courses/course-detail.html', context)
