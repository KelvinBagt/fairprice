#admin.py is used for handling admin reponsibilities and handling admin requests. In order to access the 
# admin page go to "/admin" url. 
from django.contrib import admin #importing default admin 
from .models import Journals_List, Subject, Package  #importing models from models.py
from import_export.admin import ImportExportModelAdmin #import export django model used to allow importing and exporting of different types of files  
from journals.resources import ListResource, SubjectResource, PackageResource  #importing resources of models


class ListAdmin(ImportExportModelAdmin): #allows importing and exporting for journal_list model
    resource_class = ListResource

class SubjectAdmin(ImportExportModelAdmin): #allows importing and exporting for Subject model
	resource_class = SubjectResource    

class PackageAdmin(ImportExportModelAdmin): #allows importing and exporting for Package model
	resource_class = PackageResource 	

admin.site.register(Journals_List, ListAdmin) # registering classes and models into admin.py
admin.site.register(Subject, SubjectAdmin) 
admin.site.register(Package, PackageAdmin) 
