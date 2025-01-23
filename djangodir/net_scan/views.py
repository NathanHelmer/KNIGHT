from django.shortcuts import render

# Create your views here.

def nmap_scans(request):
    return render(request, 'NMAP_Scans.html')
