import requests
from celery import shared_task
from .models import TelegramUsers,Subscriptions


@shared_task
def telegram_mailing():
    subscriptions = Subscriptions.objects.filter(is_active=True)

    for subscription in subscriptions: 
        bot_url = 'https://api.telegram.org/bot6514227741:AAHlzRf2oa66JwOPUZ8iNHApeOqfN9B3Y4c/sendMessage'
        message="Рассылка которая работает каждые 30сек"
        data={
            "chat_id":subscription.user.user_id,
            "text": message
        }
        response=requests.post(bot_url,data=data)
        if response.status_code==201:
            subscription.save()


