#forms.py is used for handling all types of forms of the fairprice website.  

from django import forms

class FilterForm(forms.Form):   
    Subject_Choices=(("ALL","ALL"),   #subject choices that will be displayed in the subject label
                     ("ACCOUNTING","ACCOUNTING"),
                     ("AGRICULTURE","AGRICULTURE"),
                     ("ALLERGY AND IMMUNOLOGY", "ALLERGY AND IMMUNOLOGY"),
                     ("ALTERNATIVE MEDICINE", "ALTERNATIVE MEDICINE"),
                     ("ANAESTHESIOLOGY", "ANAESTHESIOLOGY"), 
                     ("ANALYTICAL CHEMISTRY", "ANALYTICAL CHEMISTRY"),  
                     ("ARCHAEOLOGY", "ARCHAEOLOGY"),
                     ("ARCHITECTURE", "ARCHITECTURE"),
                     ("AREA STUDIES", "AREA STUDIES"),
                     )
    Package_Choices=(("ALL","ALL"), #package choices that will be displayed in the subject label 
                     ("Wiley","Wiley"),
                     ("T&F","T&F"),
                     ("Sage","Sage"),
                     ("Springer","Springer"),
                     ("Oxford","Oxford"),
                     ("Cambridge","Cambridge"),   )                 
    Subject = forms.ChoiceField(choices = Subject_Choices)  #using ChoiceField function to allow user to choose for the list of objects
    Search = forms.CharField(label='Search', max_length=100,required=False) 
    Package = forms.ChoiceField(choices = Package_Choices)