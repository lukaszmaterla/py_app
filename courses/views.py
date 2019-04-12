from django.shortcuts import render
from django.views import View


class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        return render(request, self.template_name, {})

