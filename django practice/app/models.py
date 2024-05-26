from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    __tableName__ = 'patient'
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40 , default=False)
    mobile = models.CharField(max_length=20,null=False, default='Mobile number')
    symptoms = models.CharField(max_length=100,null=False,default='Symptoms')
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def _str_(self):
        return self.user.first_name+" ("+self.symptoms+")"
    
class doctor_details(models.Model):     
    __tableName__ = 'doctor_details'
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='user')
    name=models.CharField(max_length=50,null=False,blank=False, default=False)
    degree=models.CharField(max_length=500,null=False,blank=False, default=False)
    mobile = models.IntegerField(default=False)    
    weekday = models.CharField(max_length=500, default=False)
    hospitalName=models.CharField(max_length=500,null=False,blank=False, default=False)
    address=models.CharField(max_length=500,null=False,blank=False, default=False)
    profile_pic =models.ImageField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=500, null=True)
    no_of_patient = models.IntegerField(null=True)
    brief = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True)
    time_in = models.TimeField()
    time_out = models.TimeField()
    created_date=models.DateTimeField(auto_now_add=True)
    last_updated_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    specilist = models.CharField(max_length=500, blank=True) 
    @property
    def _str_(self):
        return self.name
    
    @property
    def get_id(self):
        return self.user.id

class Patient_detail(models.Model):
    __tableName__ = 'Patient_detail'
    user=models.OneToOneField(User,on_delete=models.CASCADE, default=False)
    patientName = models.CharField(max_length=500,null=False,blank=False)
    gender = models.CharField(max_length=500,null=False,blank=False)
    dateofbirth = models.IntegerField(default=False)
    mobileNo = models.IntegerField(default=False)
    email = models.EmailField(default=False)
    disease = models.CharField(max_length=500,null=False,blank=False)
    desc = models.CharField(max_length=500,null=False,blank=False)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def _str_(self):
        return self.user.first_name+" ("+self.disease+")"
    
class Appointment(models.Model):
    __tableName__ = 'appointment'
    user=models.OneToOneField(User,on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=500, default=False)
    age = models.IntegerField(default=False)
    gender = models.CharField(max_length=500, default=False)
    date = models.DateField(default=False)
    time=models.TimeField(auto_now=True)
    area_name=models.CharField(max_length=500, default=False)
    email = models.EmailField(default=False)
    specilist = models.CharField(max_length=500, default=False)
    phone = models.IntegerField(default=False)
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    def _str_(self):
        return self.name
    
class my_appointment(models.Model):
    __tableName__ = 'my_appointment'
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    patientName = models.CharField(max_length=500,null=False,blank=False)
    gender = models.CharField(max_length=500,null=False,blank=False)
    mobileNo = models.IntegerField()
    age = models.DateField()
    disease = models.CharField(max_length=500,null=False,blank=False)
    date = models.DateField()
    doctorName = models.CharField(max_length=500,null=False,blank=False)
    hospitalName = models.CharField(max_length=500,null=False,blank=False)
    address=models.CharField(max_length=500,null=False,blank=False)

    def _str_(self):
        return self.patientName
    
from django.utils.translation import gettext_lazy as _

DAY_OF_THE_WEEK = {
    '1' : _('Monday'),
    '2' : _('Tuesday'),
    '3' : _('Wednesday'),
    '4' : _('Thursday'),
    '5' : _('Friday'),
    '6' : _('Saturday'), 
    '7' : _('Sunday'),
}

class DayOfTheWeekField(models.CharField):
    def _init_(self, *args, **kwargs):
        print(kwargs)
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1 
        super(DayOfTheWeekField,self)._init_(*args, **kwargs)



class time_slots(models.Model):
    __tableName__ = 'time_slots'
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time_in = models.TimeField()
    time_out = models.TimeField()
    area_name = models.CharField(max_length=500, default='area')
    dayOfTheWeek = DayOfTheWeekField(max_length=200, null=True)

    def _str_(self):
        return f"{self.time_out.strftime('%H:%M', '%I:%M%p', '%I:%M %p')}"
    
    def _str_(self):
        return f"{self.time_out.strftime('%H:%M', '%I:%M%p', '%I:%M %p')}"
   

class clinic_area(models.Model):
    __tableName__ = 'clinic_area'
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    clinic_name = models.CharField(max_length=500)
    area_name = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

class specilization(models.Model):
    __tableName__ = 'specilization'
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    specilist = models.CharField(max_length=500,default=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)