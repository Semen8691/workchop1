
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput

from core.models import CustomUser


class UserRegistrationForm(ModelForm):
    password_1 = CharField(
        max_length=20,
        min_length=6,
        widget=PasswordInput
    )

    password_2 = CharField(
        max_length=20,
        min_length=6,
        widget=PasswordInput
    )

    class Meta:
        model = CustomUser
        exclude = ('last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined')

    def check_pass(self):
        data = self.changed_data
        if data['password_1'] != data['password_2']:
            raise ValidationError('Неверный повтор пароля')
        return data['password_1']