from django.db import models


class TelegramUsers(models.Model):
    nickname=models.CharField(max_length=30,verbose_name="Никнейм")
    user_id=models.BigIntegerField(unique=True,verbose_name="ID телеграм")
    phone =models.CharField(max_length=30,verbose_name="Номер телефона")


    def __str__(self) -> str:
        return self.nickname
    

    class Meta:
        verbose_name="Пользователь Телеграм"
        verbose_name_plural="Пользователи Телеграм"


class Subscriptions(models.Model):
    user=models.ForeignKey(TelegramUsers,on_delete=models.PROTECT,verbose_name="Пользователь")
    date=models.DateTimeField(auto_now_add=True,verbose_name="Дата публикации")
    is_active=models.BooleanField(default=True,verbose_name="Подписки")


    def __str__(self) -> str:
        return f"{self.user}"
    

    class Meta:
        unique_together = ("user",)
        verbose_name="Подписка"
        verbose_name_plural="Подписки"