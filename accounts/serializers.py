from rest_framework import serializers
from .models import Users
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    token=serializers.CharField(read_only=True)


    class Meta:
        model=Users
        fields=("phone_number","password","token")


    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        refresh=RefreshToken.for_user(user)
        token=str(refresh.access_token)
        return {"phone_namber": user.phone_number,"token":token}