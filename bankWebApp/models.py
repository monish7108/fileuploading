from django.db import models

class cust_details(models.Model):
    cust_account_id=models.IntegerField(verbose_name="cust_account_id",primary_key=True)
    cust_name=models.CharField(verbose_name="cust_name",max_length=25)
    cust_address=models.TextField(verbose_name="cust_address")
    cust_dob=models.DateField(verbose_name="cust_dob", auto_now_add=True)
    cust_email=models.EmailField()
    cust_balance=models.IntegerField()

    def __str__(self):
        details=str(self.cust_account_id)+" "+self.cust_name+" "+str(self.cust_balance)+" "+self.cust_address
        return details
