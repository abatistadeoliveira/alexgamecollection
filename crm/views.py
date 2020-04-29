from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum

now = timezone.now()


def home(request):
    return render(request, 'crm/home.html',
                  {'crm': home})


@login_required
def collector_list(request):
    collector = Collector.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/collector_list.html',
                  {'collectors': collector})


@login_required
def collector_edit(request, pk):
    collector = get_object_or_404(Collector, pk=pk)
    if request.method == "POST":
        # update
        form = CollectorForm(request.POST, instance=collector)
        if form.is_valid():
            collector = form.save(commit=False)
            collector.updated_date = timezone.now()
            collector.save()
            collector = Collector.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/collector_list.html',
                          {'collectors': collector})
    else:
        # edit
        form = CollectorForm(instance=collector)
    return render(request, 'crm/collector_edit.html', {'form': form})


@login_required
def collector_delete(request, pk):
    collector = get_object_or_404(Collector, pk=pk)
    collector.delete()
    return redirect('crm:collector_list')


@login_required
def console_list(request):
    consoles = Console.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/console_list.html', {'consoles': consoles})


@login_required
def console_new(request):
    if request.method == "POST":
        form = ConsoleForm(request.POST)
        if form.is_valid():
            console = form.save(commit=False)
            console.created_date = timezone.now()
            console.save()
            consoles = Console.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/console_list.html',
                          {'consoles': consoles})
    else:
        form = ConsoleForm()
        # print("Else")
    return render(request, 'crm/console_new.html', {'form': form})


@login_required
def console_edit(request, pk):
    console = get_object_or_404(Console, pk=pk)
    if request.method == "POST":
        form = ConsoleForm(request.POST, instance=console)
        if form.is_valid():
            console = form.save()
            # console.collector = console.id
            console.updated_date = timezone.now()
            console.save()
            consoles = Console.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/console_list.html', {'consoles': consoles})
    else:
        # print("else")
        form = ConsoleForm(instance=console)
    return render(request, 'crm/console_edit.html', {'form': form})


@login_required
def console_delete(request, pk):
    console = get_object_or_404(Console, pk=pk)
    console.delete()
    return redirect('crm:console_list')


@login_required
def videogame_list(request):
    videogames = VideoGame.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/videogame_list.html', {'videogames': videogames})


@login_required
def videogame_new(request):
    if request.method == "POST":
        form = VideoGameForm(request.POST)
        if form.is_valid():
            videogame = form.save(commit=False)
            videogame.created_date = timezone.now()
            videogame.save()
            videogames = VideoGame.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/videogame_list.html',
                          {'videogames': videogames})
    else:
        form = VideoGameForm()
        # print("Else")
    return render(request, 'crm/videogame_new.html', {'form': form})


@login_required
def videogame_edit(request, pk):
    console = get_object_or_404(VideoGame, pk=pk)
    if request.method == "POST":
        form = VideoGameForm(request.POST, instance=console)
        if form.is_valid():
            videogame = form.save()
            # videogame.collector = videogame.id
            videogame.updated_date = timezone.now()
            videogame.save()
            videogames = VideoGame.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/videogame_list.html', {'consoles': consoles})
    else:
        # print("else")
        form = VideoGameForm(instance=console)
    return render(request, 'crm/videogame_edit.html', {'form': form})


@login_required
def videogame_delete(request, pk):
    videogame = get_object_or_404(VideoGame, pk=pk)
    videogame.delete()
    return redirect('crm:videogame_list')


@login_required
def summary(request, pk):
    collector = get_object_or_404(Collector, pk=pk)
    collectors = Collector.objects.filter(created_date__lte=timezone.now())
    consoles = Console.objects.filter(coll_name=pk)
    videogames = VideoGame.objects.filter(coll_name=pk)
    sum_console_charge = Console.objects.filter(coll_name=pk).aggregate(Sum('console_price'))
    sum_videogame_charge = VideoGame.objects.filter(coll_name=pk).aggregate(Sum('videogame_charge'))
    return render(request, 'crm/summary.html', {'collectors': collectors,
                                                'videogames': videogames,
                                                'consoles': consoles,
                                                'sum_console_charge': sum_console_charge,
                                                'sum_videogame_charge': sum_videogame_charge, })
