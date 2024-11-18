from django.shortcuts import render,redirect,get_object_or_404
from .forms import AccountForm,TransferForm
from .models import Account,Transfer
from django .contrib import messages
# from django .http import HttpResponse


def account_list(request):
    accounts = Account.objects.all()
    return render(request,'accounts/account_list.html',{'accounts':accounts})


def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
        return render(request,'accounts/account_form.html',{'form': form})


def account_update(request,pk):
    account = get_object_or_404(Account,pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
        return render(request,'accounts/account_form.html',{'form':form})

def account_delete(request,pk):
    account = get_object_or_404(Account,pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request,'accounts/account_confirm_delete.html',{'account':account})


def transfer_view(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']
            if from_account == to_account:
                messages.error(request,"Cannot transfer to the same account.")

            elif amount <= 0:
                messages.error(request,"Transfer amount must be greater than zero.")

            elif from_account.balance < amount:
                messages.error(request,"Insufficient funds in the source account.")


            else:
                form.save()
                # return redirect('transfer_success')
                messages.success(request,'successfully')
            return redirect('transfer')

    else:
        form = TransferForm()
        return render(request,'accounts/transfer.html',{'form': form})





def transfer_history(request):
    transfers = Transfer.objects.all()
    return render(request,'accounts/transfer_history.html',{'transfers':transfers})



