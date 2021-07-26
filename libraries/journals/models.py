#model.py is used for creating/storing different models. The each attribute of the model represents
# a databse field  
from django.db import models

class Subject(models.Model): #Subject model that stores all the Subject names
    Name = models.CharField('Subject', max_length=100, blank=True)

    def __str__(self):
        return self.Name

class Package(models.Model): #Package model that stores all the Package names
    Name = models.CharField('Package', max_length=100, blank=True)

    def __str__(self):
        return self.Name        

class Journals_List(models.Model): #Journals_List model that stores all the attributes of a journal       
      #Subject attribute is linked to the Subject model using foreign key
      Subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.PROTECT)
      Title = models.CharField('Journal name', max_length=100) 
      URL = models.URLField(max_length=200, blank=True,  null=True)
      P_ISSN = models.CharField(max_length=100, blank=True, null=True)
      E_ISSN = models.CharField(max_length=100, blank=True, null=True)
      #Package attribute is linked to the Package model using foreign key
      Package = models.ForeignKey(Package,blank=True,null=True, on_delete=models.PROTECT)  
      
      class Meta:
        ordering=('Title',)
  
      def __str__(self):
        return self.Title 
        
