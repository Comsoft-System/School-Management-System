from django.db import models
from student.models import Classes, GRRegister, Section

# Basic Tables
class FeeType(models.Model):
    fee_code = models.AutoField(primary_key = True)
    fee_type = models.CharField(max_length = 100)
    fee_remarks = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.fee_type

class Concession(models.Model):
    concession_code = models.AutoField(primary_key = True)
    concession_type = models.CharField(max_length = 100)
    concession_amount = models.IntegerField(default = 0, null = True, blank = True)
    concession_persent = models.IntegerField(default = 0, null = True, blank = True)
    concession_remarks = models.TextField(null = True, blank = True)

    def __str__(self):
        return f'{self.concession_type} - {self.concession_persent}'

# Operative Tables
class ClassFee(models.Model):
    class_code = models.ForeignKey(Classes, on_delete = models.CASCADE)
    fee_amount = models.IntegerField()  

    def __str__(self):
        return str(self.class_code.class_name)

class Fee(models.Model):
    # MONTH_CHOICES = [
    #     ('January', 'January'),
    #     ('February', 'February'),
    #     ('March', 'March'),
    #     ('April', 'April'),
    #     ('May', 'May'),
    #     ('June', 'June'),
    #     ('July', 'July'),
    #     ('August', 'August'),
    #     ('September', 'September'),
    #     ('October', 'October'),
    #     ('November', 'November'),
    #     ('December', 'December'),
    # ]

    gr_number = models.IntegerField()
    class_code = models.CharField(max_length = 200)
    section_code = models.CharField(max_length = 200)
    due_amount = models.IntegerField(blank=True, null=True)
    submit_amount = models.IntegerField()
    # mounth = models.CharField(max_length = 50, choices = MONTH_CHOICES)
    fee_status = models.BooleanField()

    def __str__(self):
        return str(self.gr_number)