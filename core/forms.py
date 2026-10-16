from django import forms
from .models import Farmer, Land, Crop, Investor


class FarmerForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        label="Username"
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )

    class Meta:
        model = Farmer
        fields = [
            "username",
            "password",
            "name",
            "phone",
            "email",
            "address",
        ]


class LandForm(forms.ModelForm):

    class Meta:
        model = Land
        fields = [
            "location",
            "district",
            "state",
            "area_acres",
            "soil_type",
            "land_photo",
        ]


class CropForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = [
            "crop_name",
            "variety",
            "cultivation_area",
            "expected_quantity",
            "expected_harvest_date",
            "expected_selling_price",
        ]

        widgets = {
            "expected_harvest_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
class InvestorForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        label="Username"
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model = Investor
        fields = [
            "username",
            "password",
            "confirm_password",
            "name",
            "phone",
            "email",
            "address",
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:

                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data