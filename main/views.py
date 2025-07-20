from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import RefurbishedLaptop
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking 
from .forms import RefurbishedLaptopForm

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def refurbished(request):
    laptops = RefurbishedLaptop.objects.filter(available=True)
    return render(request, 'refurbished.html', {'laptops': laptops})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Your service has been booked successfully!")
            return redirect('my_bookings')
        else:
            messages.error(request, "There was a problem with your booking. Please try again.")
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status != 'Pending':
        messages.error(request, "Only pending bookings can be deleted.")
        return redirect('my_bookings')

    booking.delete()
    messages.success(request, "Your booking has been cancelled.")
    return redirect('my_bookings')


def contact(request):
    return render(request, 'contact.html')

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)



from django.contrib.auth.decorators import user_passes_test

def staff_required(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(staff_required)
def admin_dashboard(request):
    if request.method == 'POST':
        form = RefurbishedLaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New laptop added successfully!")
            return redirect('admin_dashboard')
    else:
        form = RefurbishedLaptopForm()

    bookings = Booking.objects.all().order_by('-created_at')
    laptops = RefurbishedLaptop.objects.all()
    return render(request, 'custom_admin/dashboard.html', {
        'bookings': bookings,
        'laptops': laptops,
        'form': form
    })


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was updated successfully.")
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})