from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import LicenseOrder
from .forms import LicenseForm
from django.views.generic import ListView,UpdateView
from django.template.loader import render_to_string
# Create your views here.

def index(request):

    return render(request,'Dashboard.html')

def manage(request):
    
    return render(request,'manage.html')

def orders(request):
    
    return render(request,'orders.html')

def profile(request):
    
    return render(request,'profile.html')

def contact(request):
    
    return render(request,'contact.html')

def logout(request):
    
    return render(request,'Logout.html')

def vendors(request):
    
    return render(request,'vendors.html')

def license_order(request):
    data=LicenseOrder.objects.all()

    context = {
        'data':data,
    }
    return render(request,'license_order.html',context)

def Edit(request):
    data=LicenseOrder.objects.all()

    context = {
        'data':data,
    }
    return redirect(request,'license_order.html',context)



def Update(request,id):

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        subscription_id= request.POST.get('subscription_id')
        commitment_or_billing = request.POST.get('commitment_or_billing')
        product_name = request.POST.get('product_name')
        domain_name = request.POST.get('domain_name')
        qty = request.POST.get('qty')
        license_type = request.POST.get('license_type')
        vendor_name = request.POST.get('vendor_name')
        current_active_qty = request.POST.get('current_active_qty')
        erp =request.POST.get('erp')
        customer =request.POST.get('customer')
        qut_no = request.POST.get('qut_no')
        invoice_no = request.POST.get('invoice_no')
        create_sales_order = request.POST.get('create_sales_order')

        data = LicenseOrder(
            id=id,
            start_date=start_date,
            subscription_id=subscription_id,
            commitment_or_billing=commitment_or_billing,
            product_name=product_name,
            domain_name=domain_name,
            qty=qty,
            license_type=license_type,
            vendor_name=vendor_name,
            current_active_qty=current_active_qty,
            erp=erp,
            customer=customer,
            qut_no=qut_no,
            invoice_no=invoice_no,
            create_sales_order=create_sales_order,

        )

        data.save()
        return redirect('home')
    
    return render(request,'license_order.html')


def Delete(request,id):
    data = LicenseOrder.objects.filter(id=id)
    data.delete()
    context = {
        'data':data
    }
    
    return redirect('home')
def add(request):
    if request.method == "POST":

        start_date = request.POST.get('start_date')
        subscription_id= request.POST.get('subscription_id')
        commitment_or_billing = request.POST.get('commitment_or_billing')
        product_name = request.POST.get('product_name')
        domain_name = request.POST.get('domain_name')
        qty = request.POST.get('qty')
        license_type = request.POST.get('license_type')
        vendor_name = request.POST.get('vendor_name')
        current_active_qty = request.POST.get('current_active_qty')
        erp =request.POST.get('erp')
        customer =request.POST.get('customer')
        qut_no = request.POST.get('qut_no')
        invoice_no = request.POST.get('invoice_no')
        create_sales_order = request.POST.get('create_sales_order')

        data = LicenseOrder(
            
            start_date=start_date,
            subscription_id=subscription_id,
            commitment_or_billing=commitment_or_billing,
            product_name=product_name,
            domain_name=domain_name,
            qty=qty,
            license_type=license_type,
            vendor_name=vendor_name,
            current_active_qty=current_active_qty,
            erp=erp,
            customer=customer,
            qut_no=qut_no,
            invoice_no=invoice_no,
            create_sales_order=create_sales_order,

        )
        data.save()
        return redirect('home')


    return render(request,'license_order.html')

    