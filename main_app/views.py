from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import CleaningBrush, Played, Record
from .forms import PlayedForm
# Create your views here.

def home(request):
  return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
  records = Record.objects.all()
  return render(request, 'records/index.html', { 'records':records})

def records_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  played_form = PlayedForm()
  # Get the cleaning brushes the record doesn't have.
  cleaning_brushes_record_doesnt_have = CleaningBrush.objects.exclude(id__in = record.cleaning_brush.all().values_list('id'))
  return render(request, 'records/detail.html', {'record':record, 'played_form':played_form, 'cleaning_brush': cleaning_brushes_record_doesnt_have})

def add_played(request, record_id):
  form = PlayedForm(request.POST)
  if form.is_valid():
    new_played = form.save(commit = False)
    new_played.record_id = record_id
    new_played.save()
  return redirect ('detail', record_id=record_id)

def assoc_cleaning_brush(request, record_id, cleaning_brush_id):
  Record.objects.get(id=record_id).cleaning_brush.add(cleaning_brush_id)
  return redirect('detail', record_id=record_id)

def remove_cleaning_brush(request, record_id, cleaning_brush_id):
    Record.objects.get(id=record_id).cleaning_brush.remove(cleaning_brush_id)
    return redirect('detail', record_id=record_id)



