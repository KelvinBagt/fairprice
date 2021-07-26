#resources.py maps import export representations of objects and handles importing and exporting data   
from import_export import resources
from journals.models import Journals_List, Subject, Package

class ListResource(resources.ModelResource):
	
    class Meta:
        model = Journals_List 

class SubjectResource(resources.ModelResource):
	
    class Meta:
        model = Subject

class PackageResource(resources.ModelResource):
	
    class Meta:
        model = Package                  