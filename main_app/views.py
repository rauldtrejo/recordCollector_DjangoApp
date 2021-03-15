from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import CleaningBrush, Record
from .forms import CleaningForm, PlayedForm, RecordForm

# Create your views here.

def home(request):
  return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def records_index(request):
  records = Record.objects.filter(user=request.user)
  return render(request, 'records/index.html', { 'records':records})

@login_required
def records_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  played_form = PlayedForm()
  # Get the cleaning brushes the record doesn't have.
  cleaning_brushes_record_doesnt_have = CleaningBrush.objects.exclude(id__in = record.cleaning_brush.all().values_list('id'))
  return render(request, 'records/detail.html', {'record':record, 'played_form':played_form, 'cleaning_brush': cleaning_brushes_record_doesnt_have})

@login_required
def add_played(request, record_id):
  form = PlayedForm(request.POST)
  if form.is_valid():
    new_played = form.save(commit = False)
    new_played.record_id = record_id
    new_played.save()
  return redirect ('detail', record_id=record_id)

@login_required
def assoc_cleaning_brush(request, record_id, cleaning_brush_id):
  Record.objects.get(id=record_id).cleaning_brush.add(cleaning_brush_id)
  return redirect('detail', record_id=record_id)

@login_required
def remove_cleaning_brush(request, record_id, cleaning_brush_id):
    Record.objects.get(id=record_id).cleaning_brush.remove(cleaning_brush_id)
    return redirect('detail', record_id=record_id)

@login_required
def add_record(request):
 record_form = RecordForm(request.POST or None)
  # if the form was posted and valid
 if request.POST and record_form.is_valid():
    # save new instance of a cat
    new_record = record_form.save(commit=False)
    new_record.user = request.user
    new_record.save()
    # redirect to index
    return redirect('index')
 else:
    # render the page with the new cat form
    return render(request, 'records/add.html', { 'record_form': record_form })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def records_delete(request, record_id):
  Record.objects.get(id=record_id).delete()
  return redirect('index')


@login_required
def records_edit(request, record_id):
  # get a reference to a cat
  record = Record.objects.get(id=record_id)
  # build a form for the cat filling it with values from the instance or values from the POST request
  record_form = RecordForm(request.POST or None, instance=record)
  if request.POST and record_form.is_valid():
    # save changes to the cat
    record_form.save()
    # redirect to the detail page
    return redirect('detail', record_id=record_id)
  else:
    return render(request, 'records/edit.html', { 'record': record, 'record_form': record_form })

@login_required
def add_cleaning_product(request):
  cleaning_form = CleaningForm(request.POST or None)
  # if the form was posted and valid
  if request.POST and cleaning_form.is_valid():
    # save new instance of a cat
    cleaning_form.save(commit=True)
    # redirect to index
    return redirect('cleaning_products')
  else:
    # render the page with the new cat form
    return render(request, 'cleaningEquipment/add.html', { 'cleaning_form': cleaning_form })


@login_required
def cleaning_equipment_index(request):
  equipment = CleaningBrush.objects.all()
  return render(request, 'cleaningEquipment/index.html', { 'equipment':equipment})

@login_required
def cleaning_equipment_delete(request, equipment_id):
  CleaningBrush.objects.get(id=equipment_id).delete()
  return redirect('cleaning_products')

