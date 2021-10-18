from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs.update(
            {"placeholder": "Fullname", "autofocus": None}
        )

        self.fields["email"].widget.attrs.update({"placeholder": "Email"})
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Username"}
        )
        self.fields["password1"].widget.attrs.update(
            {"placeholder": "Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Confirmation Password"}
        )

        for name, field in self.fields.items():
            field.widget.attrs["required"] = None


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "name",
            "short_intro",
            "address",
            "bio",
            "profile_image",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
