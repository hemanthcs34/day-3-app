from django.shortcuts import render

# Create your views here.
def add_numbers(request):
    result = None
    error = None
    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')

        try:
            sum = float(num1) + float(num2)
            result = f"the sum is: { sum }"
            print(result)
        except:
            error = "something went wrong"
            print(error)

    return render(request,'add.html',{'result': result,'error': error})

def calc(request):
    result = None
    error = None
    if request.method == "POST":
        amount = request.POST.get('amount')
        time = request.POST.get('time')
        rate = request.POST.get('rate')

        try:
            SI = (float(amount) * float(time) * float(rate))/100
            result = f"the value is: { SI }"
            
        except:
            error = "something went wrong in pnr"
        

    return render(request,'pnr.html',{'result': result,'error': error})