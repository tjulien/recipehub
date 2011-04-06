from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name') 
