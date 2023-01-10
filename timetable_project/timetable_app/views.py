from django.shortcuts import render
def timetable(request):
    return render(request,'timetable_app/timetable.html')
def secmap(request):
    return render(request,'timetable_app/secmap.html')
def firstyearblock(request):
    return render(request,'timetable_app/firstyearblock')         