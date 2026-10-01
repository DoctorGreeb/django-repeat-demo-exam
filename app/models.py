from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

type_choices = (
    ('Аудитория', 'Аудитория'),
    ('Коворкинг','Коворкинг'),
    ('Кинозал','Кинозал')
)

payment_choices = (
    ('При очном посещении','При очном посещении'),
    ('По системе СБП','По системе СБП'),
    ('Завершено','Завершено')
)

status_choices = ( 
    ('Новая','Новая'),
    ('Мероприятие назначено','Мероприятие назначено')
)

class User(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
class Zayavka(models.Model):
    type = models.CharField(max_length=30, verbose_name='Тип помещения', choices=type_choices)
    payment = models.CharField(max_length=30, verbose_name='Вид оплаты', choices=payment_choices)
    status = models.CharField(max_length=30, verbose_name='Статус бронирования', choices=status_choices)
    date = models.DateField(verbose_name='Дата')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.user.phone} -- {self.type} -- {self.status}'
    
    class Meta:
        verbose_name = 'Заявка на бронирование'
        verbose_name_plural = 'Заявки на бронирование'
        
class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    zayavka = models.OneToOneField(Zayavka, on_delete=models.DO_NOTHING, verbose_name='Заявка')
    
    def __str__(self):
        return f'{self.user.phone} -- {self.createdAt}'
    
    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'
    
