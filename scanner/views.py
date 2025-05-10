from django.shortcuts import render
from .scanner import run_scan

def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        results = run_scan(url)
        return render(request, "scanner/result.html", {"results": results, "url": url})
    return render(request, "scanner/index.html")
