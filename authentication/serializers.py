from rest_framework import serializers 
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only = True,
        required = True,
        help_text = "Password Confirmation",
        style = {'input_type':"password"}
    )

    password2 = serializers.CharField(
        write_only = True,
        required = True,
        help_text = "Password Confirmation",
        style = {'input_type':"password"}
    )


    class Meta:
        model = User
        fields = ('email', 'phone', 'password1', 'password2')