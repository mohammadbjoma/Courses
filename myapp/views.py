import json
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Course
# Create your views here.
def coursesPage(request):
    return render(request,"index.html")


def loginP(request):
    return render(request,"Account.html")

def course_data(request):
    json_path = os.path.join(settings.BASE_DIR, 'myapp', 'data', 'course.json')
    with open(json_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)


def add_course(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        hours = request.POST.get('hours')
        student = request.POST.get('student')
        image_file = request.FILES.get('image')
        course = Course(
            title=title,
            description=description,
            hours=hours,
            student=student,
            image=image_file
        )
        course.save()
        if image_file:
            image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
            with open(image_path, 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
            image_url = settings.MEDIA_URL + image_file.name
        else:
            image_url = ""
            
        json_dir = os.path.join(settings.BASE_DIR, 'myapp', 'data')
        json_path = os.path.join(json_dir, 'course.json')

        with open(json_path, 'r') as f:
            data = json.load(f)

        new_course = {
            'title': title,
            'description': description,
            'hours': hours,
            'student': student,
            'image': image_url
        }
        data.append(new_course)

        with open(json_path, 'w') as f:
            json.dump(data, f, indent=4)

        return redirect('/')  

    return render(request, 'index.html')
