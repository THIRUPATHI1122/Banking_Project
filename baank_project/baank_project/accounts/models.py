from django.db import models
from django.utils import timezone

class Account(models.Model):
    ACCOUNT_TYPE = [
        ('Saving','Saving'),
        ('Current', 'Current'),
        ('Overdraft', 'Overdraft'),
    ]

    acc_name = models.CharField(max_length=20)
    acc_no = models.CharField(max_length=15,unique=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    acc_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    balance = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.acc_name} - {self.acc_no}"

class Transfer(models.Model):
    from_account = models.ForeignKey(Account,related_name='transfer_from',on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='transfer_to', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    amount_from = models.IntegerField(editable=False,default=0)
    amount_to = models.IntegerField(editable=False, default=0)
    from_status = models.CharField(max_length=10,editable=False,default='debited')
    to_status = models.CharField(max_length=10, editable=False, default='credited')
    datetime = models.DateTimeField(default=timezone.now,editable=False)

    def save(self,*args,**kwargs):
        if self.from_account.balance >= self.amount:
            self.from_account.balance -= self.amount
            self.to_account.balance += self.amount

            self.amount_from = self.amount
            self.amount_to = self.amount

            self.from_status = 'Debited'
            self.to_status = 'Credited'

            self.from_account.save()
            self.to_account.save()

            super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.from_account} to {self.to_account} of {self.amount} on {self.datetime}"



