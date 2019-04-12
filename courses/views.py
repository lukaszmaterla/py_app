from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CourseModelForm
from .models import Course


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'objects_list': self.get_queryset()}
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, *args, **kwargs):
        form_class = CourseModelForm()
        context = {'form': form_class}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_class = CourseModelForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            form_class = CourseModelForm()
        context = {'form': form_class}
        return render(request, self.template_name, context)

#
# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=1)


class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

