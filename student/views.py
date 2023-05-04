from django.shortcuts import render, redirect
from .models import student_data,student_school_data
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def student_all(request):
    query_set = student_school_data.objects.select_related('student').all()[:20]
    paginator = Paginator(query_set,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # 'student_details': query_set,
        'page_obj': page_obj
       }
    return render(request, 'student_home.html',context )

@csrf_exempt
def student_create(request): 
    try:
        if request.method == 'POST':
            data = request.POST
            #print("data:",data)
            if 'Commute' in data:
                commute = True
            else:
                commute = False
            query_set = student_data.objects.create(first_name = data['fname'],last_name=data['lname'],email=data['email'],Address_1=data['address1'],Address_2=data['address2'],Guardian_Cell_phone=data['mobile'])
            query_set.save()
            query_set_2 = student_school_data.objects.create(c_class=data['class'],Percentage=data['percentage'],Commute=commute,student=query_set)
            query_set_2.save()   
        else:
            return render(request, 'data_form.html')
    except Exception as e:
        print("Exception:",e)
    return redirect('all_data')    
    
def student_update(request,pk):
    try:
        query_set = student_data.objects.get(pk=pk)
        query_set2 = query_set.school_detail.filter(student=pk).first()
        if request.method == 'POST':
            data = request.POST
            if 'Commute' in data:
                commute = True
            else:
                commute = False 
            try:
                query_set = student_data.objects.get(pk=pk)
                query_set2 = query_set.school_detail.filter(student=pk).first()
                query_set2.Percentage = data['percentage']
                query_set2.Commute = commute
                query_set2.c_class = data['class']
                query_set.first_name = data['fname']
                query_set.last_name=data['lname']
                query_set.email=data['email']
                query_set.Address_1=data['address1']
                query_set.Address_2=data['address2']
                query_set.Guardian_Cell_phone=data['mobile']
                query_set.save()
                query_set2.student = query_set
                query_set2.save()
            except Exception as e:
                print(e)
        else:
            context = {
                'student_details': query_set,
                'school_details': query_set2
                }
            return render(request,'data_form.html',context)
    except Exception as e:
        print("Exception:",e)
    return redirect('all_data')

def student_delete(request,pk):
    query_set = student_data.objects.filter(pk=pk)
    query_set.delete()
    return redirect('all_data')
