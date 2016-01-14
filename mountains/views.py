from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q # allows complex queries when searching
from django.http import HttpResponse
from . models import Mountain, MountainRange
from . forms import MountainForm, MountainCrispySearchForm, MountainRangeForm

def mountain_list(request):
    mountains = Mountain.objects.all().order_by('name')
    return render(request, 'mountains/mountain_list.html', {'mountains': mountains})

def mountain_detail(request, pk):
    mountain = get_object_or_404(Mountain, pk=pk)
    return render(request, 'mountains/mountain_detail.html', {'mountain': mountain})

def mountain_new(request):
    if request.method == "POST":
        form = MountainForm(request.POST) # create a mountain form instance
    
        if form.is_valid():
            mountain = form.save()
            return redirect("mountain_detail", pk=mountain.pk)
    else:
        form = MountainForm()
    
    return render(request, "mountains/mountain_edit.html", {'form': form})



def mountain_edit(request, pk):
    mountain = get_object_or_404(Mountain, pk=pk)

    if request.method == "POST":
        form = MountainForm(request.POST, request.FILES, instance=mountain) # create a mountain form instance
    
        if form.is_valid():
            mountain = form.save()
            return redirect("mountain_detail", pk=mountain.pk)
    else:
        form = MountainForm(instance=mountain)
    
    return render(request, "mountains/mountain_edit.html", {'form': form})

def mountain_results(request):
    # process form data
    if request.method == "POST":
        # create a form instance with data from the request
        form = MountainCrispySearchForm(request.POST)
        # check validity of form
        if form.is_valid():
            
            # process data - should use .cleaned_data method after checking .is_valid
            query = form.cleaned_data.get("text", None)
            mountain_ranges = form.cleaned_data.get('mountain_range', [])

            # search text
            mountains = Mountain.objects.filter(Q(description__contains=query) | Q(name__contains=query))
            # then mountain ranges
            if (len(mountain_ranges) > 0):
                mountains = mountains.filter(mountain_range__in=mountain_ranges)
            
            return render(request, "mountains/mountain_advanced_search.html", {'mountains': mountains, 'query': query, 'form': form})
    else:
        form = MountainSearchForm()

    return render(request, 'mountains/mountain_advanced_search.html', {'form': form})


def mountain_advanced_search(request):
    # process form data
    if request.method == "POST":
        # create a form instance with data from the request
        form = MountainCrispySearchForm(request.POST)
        # check validity of form
        if form.is_valid():
            
            # process data
            query = form.cleaned_data.get("text", None)
            mountain_ranges = form.cleaned_data.get('mountain_range', [])

            # search text
            mountains = Mountain.objects.filter(Q(description__contains=query) | Q(name__contains=query))
            # then mountain ranges
            if (len(mountain_ranges) > 0):
                mountains = mountains.filter(mountain_range__in=mountain_ranges)
            
            return render(request, "mountains/mountain_results.html", {'mountains': mountains, 'query': query, 'form': form})
    else:
        form = MountainSearchForm()

    return render(request, 'mountains/mountain_advanced_search.html', {'form': form})

def see_marmot(request):

    pk = None
    if request.method == 'GET':
        pk = request.GET['pk']

    n_marmots = 0
    if pk:
        mountain = Mountain.objects.get(id=int(pk))
        if mountain:
            # can you call a class method here instead? probably
            mountain.see_marmot()
            n_marmots = mountain.number_of_marmots_seen
            mountain.save()

    return HttpResponse(n_marmots)

def mountain_range_list(request):
    mountain_ranges = MountainRange.objects.all().order_by('name')
    return render(request, "mountains/mountain_range_list.html", {'mountain_ranges': mountain_ranges})

def mountain_range_detail(request, pk):
    mountain_range = get_object_or_404(MountainRange, pk=pk)
    return render(request, "mountains/mountain_range_detail.html", {'mountain_range': mountain_range})

def mountain_range_new(request):
    if request.method == "POST":
        form = MountainRangeForm(request.POST) # create a mountain form instance
    
        if form.is_valid():
            mountain_range = form.save()
            return redirect("mountain_range_detail", pk=mountain_range.pk)
    else:
        form = MountainRangeForm()
    
    return render(request, "mountains/mountain_range_edit.html", {'form': form})
