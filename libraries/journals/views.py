#views.py is used for handling user request by returning a web response. 
from django.shortcuts import render
from .models import Journals_List, Subject, Package
from .forms import FilterForm
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import Http404

def journal(request):
    submitbutton = request.POST.get("submit")
    Subject = ''
    Search = ''
    Package = ''
    result = ''

    form = FilterForm(request.POST or None) #accesing the form data using POST 
    if form.is_valid():
        Subject = form.cleaned_data.get("Subject") #accessing user choice of subject
        Search = form.cleaned_data.get("Search")  #accessing user choice of search
        Package = form.cleaned_data.get("Package")  #accessing user choice of package
        #used objects.filter() function to filter the data based on user requests and choices
        if Subject !='ALL':
            result = Journals_List.objects.filter(Subject__Name__icontains=Subject)
            if Search != ' ':
                result = result.filter(Title__icontains=Search)
                if Package != 'ALL':
                    result = result.filter(Package__Name__icontains=Package)
        elif Subject == 'ALL':   
            if Search != ' ':
                result = Journals_List.objects.filter(Q(Title__icontains=Search) |
            Q(E_ISSN__icontains=Search) | Q(P_ISSN__icontains=Search) )
                if Package != 'ALL':
                    result = result.filter(Package__Name__icontains=Package)   
            else : 
                result = Journals_List.objects.filter(Subject__Name__icontains=Package)
        
                     
    else: 
        result = Journals_List.objects.all()        
    p = Paginator(result, 15)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)  

    context= {'result': page,'form': form, 'Subject':Subject, 'Search':Search, 'Package': Package}

    return render(request, 'journals/journals.html', context)    #returning all the data in form of web response         

def journal_detail(request, journal_id):
    try:
        journal= Journals_List.objects.get(id=journal_id)
    except Journals_List.DoesNotExist:    
        raise Http404('pet not found')

    return render(request,'journals/journal_detail.html',{'journal':journal}) 