from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadModelForm

# Create your views here.
def Lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads,
    }
    return render(request, "Leads/leads_list.html", context)
    

def Lead_detail(request, pk):
    details = Lead.objects.get(pk=pk)
    context = {
        "details":details,
    }
    return render(request, "Leads/lead_detail.html", context)


def Lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
            
    context = {
        "form":form
    }
    return render(request, "Leads/lead_create.html", context)