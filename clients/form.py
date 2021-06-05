
from django import forms
from clients.users import Users

from ansible.plugins.filter.mathstuff import unique
from ansible.parsing.utils.addresses import label


class buyer(forms.ModelForm):

    #image = forms.FileField()  #FOR UPLOAD (MODEL IMPOSSIBLE)
    
    class Meta:
        model = Users
        fields = "__all__"
    
    
class seller(forms.Form):
    sellerName = forms.CharField(max_length=30, label="Enter seller name")
    sellerEmail = forms.EmailField(max_length=30, label="Enter seller Email")
        