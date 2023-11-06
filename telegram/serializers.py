from rest_framework import serializers
from .models import TelegramUsers,Subscriptions

# Serializer telegram user
class TelegramUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=TelegramUsers
        fields=("id","nickname","user_id","phone")



# Serializer subscriptions
class SubscriptionsSerializers(serializers.ModelSerializer):
    user_id=serializers.IntegerField(source="user.user_id")
    class Meta:
        model=Subscriptions
        fields=("id","user_id","date","is_active",)


    def create(self, validated_data):
        user_registered = validated_data.pop('user').get('user_id')
        registered = TelegramUsers.objects.get(user_id=user_registered)
        user = Subscriptions.objects.create(user=registered)
        return user
    

    
    





