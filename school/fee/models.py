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
    concession_amount = models.IntegerField(default = 0)
    concession_persent = models.IntegerField(default = 0)
    concession_remarks = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.concession_type

# Operative Tables
class ClassFee(models.Model):
    class_code = models.ForeignKey(Classes, on_delete = models.CASCADE)
    fee_amount = models.IntegerField()

    def __str__(self):
        return str(self.class_code)

class Fee(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]

    gr_number = models.ForeignKey(GRRegister, on_delete = models.CASCADE)
    class_code = models.ForeignKey(Classes, on_delete = models.CASCADE)
    section_code = models.ForeignKey(Section, on_delete = models.CASCADE)
    due_amount = models.IntegerField()
    submit_amount = models.IntegerField()
    mounth = models.CharField(max_length = 50, choices = MONTH_CHOICES)
    fee_status = models.BooleanField()

    def __str__(self):
        return str(self.gr_number)