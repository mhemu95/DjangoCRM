from django.shortcuts import render
from .models import Lead

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