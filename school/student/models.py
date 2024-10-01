from django.db import models

# Basic Tables
class Classes(models.Model):
    class_code = models.AutoField(primary_key = True)
    class_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.class_name

class Section(models.Model):
    section_code = models.AutoField(primary_key = True)
    section_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.section_name

class Session(models.Model):
    session_code = models.AutoField(primary_key = True)
    session_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.session_name
    
# Operative Tables
class GRRegister(models.Model):
    gr_number = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    father_name = models.CharField(max_length = 100)
    address = models.TextField()
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_admission = models.DateField()
    class_of_admission = models.ForeignKey(Classes, on_delete = models.CASCADE)
    last_school = models.CharField(max_length = 100, null = True, blank = True)
    cell_number_1 = models.CharField(max_length = 15)
    cell_number_2 = models.CharField(max_length = 15, null = True, blank = True)
    location = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10, choices = [('Male', 'Male'), ('Female', 'Female')])
    class_of_removal = models.ForeignKey(Classes, null = True, blank = True, on_delete = models.CASCADE, related_name = 'removed_students')
    date_of_removal = models.DateField(null = True, blank = True)
    present = models.BooleanField(default = True)

    def __str__(self):
        return str(self.gr_number)

class ClassRegister(models.Model):
    gr_number = models.ForeignKey(GRRegister, on_delete = models.CASCADE)
    class_code = models.ForeignKey(Classes, on_delete = models.CASCADE)
    section_code = models.ForeignKey(Section, on_delete = models.CASCADE)
    session_code = models.ForeignKey(Session, on_delete = models.CASCADE)
    present = models.BooleanField(default = True)

    def __str__(self):
        return str(self.gr_number)