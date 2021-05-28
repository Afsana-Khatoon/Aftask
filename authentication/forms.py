from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean(self):
        user_name = self.cleaned_data.get('username')
        if user_name[0] not in ['a', 'A'] or user_name[-1] not in ['0', '1']:
            self._errors['username'] = self.error_class(
                ['Username should startswith \'A\' or \'a\' and endswith \'0\' or \'1\''])
