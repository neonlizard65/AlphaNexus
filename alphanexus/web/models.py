from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class Developer(models.Model):
    name = models.CharField(verbose_name="Название", unique=True)
    logo = models.ImageField(verbose_name="Логотип", blank = True, null = True)
    requisites = models.CharField(verbose_name="Номер счета")
    email = models.EmailField(verbose_name="Почта")
    youtube = models.CharField(verbose_name="Канал на Youtube", blank = True, null = True)
    bio = models.TextField(verbose_name="Доп. информация", blank = True, null = True)
    creator = models.ForeignKey('CustomUser', verbose_name="Создатель", on_delete=models.CASCADE, related_name="developer_creator", blank = True, null = True, default=None)
    
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    
class Country(models.Model):
    name = models.CharField(verbose_name="Название")
    code = models.CharField(verbose_name="Код", max_length=3)
    
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name="Название")
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(verbose_name="Название")
    release = models.DateField(verbose_name="Дата выхода", default=now)
    developer = models.ForeignKey(Developer, verbose_name="Компания", on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Доп. информация")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        
    def __str__(self):
        return f"{self.name} ({self.release.year})"
    
    def __repr__(self):
        return f"{self.name} ({self.release.year})"

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="Почта", unique=True)
    phone = models.CharField(verbose_name="Телефон")
    avatar = models.ImageField(verbose_name="Аватар", blank = True, null = True, default=None)
    background = models.ImageField(verbose_name="Фон", blank = True, null = True, default=None)
    is_private = models.BooleanField(verbose_name="Закрытый профиль", null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name="Страна", on_delete=models.CASCADE, blank=True, null=True, default=None)
    bio = models.TextField(verbose_name="Доп. информация", blank = True, null = True, default=None)
    developer = models.ForeignKey(Developer, verbose_name="Компания", on_delete=models.CASCADE, null=True, blank=True)
    wishlist = models.ManyToManyField(Product, verbose_name="Список желаемых", related_name="wishlist", blank = True, default=None)
    cart = models.ManyToManyField(Product, verbose_name="Корзина", related_name="cart", blank = True, default=None)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
    def __str__(self):
        return f"{self.username}"
    
    def __repr__(self):
        return f"{self.username}"
    
class Media(models.Model):
    content = models.ImageField(verbose_name="Изображение")
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Медиа"
        verbose_name_plural = "Медиа"
        
    
class CDKey(models.Model):
    content = models.CharField(verbose_name="Ключ")
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    is_redeemed = models.BooleanField(verbose_name="Исчерпан", default=False)
    
    class Meta:
        verbose_name = "Ключ"
        verbose_name_plural = "Ключи"
        
    def __str__(self):
        return f"{self.product} {self.content}"
    
    def __repr__(self):
        return f"{self.product} {self.content}"

class Post(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, verbose_name="Автор", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Дата и время", default=now)
    header = models.CharField(verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    media = models.ImageField(verbose_name="Изображение", blank=True, null=True, default=None)
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        
    def __str__(self):
        return f"{self.author} - {self.header}"
    
    def __repr__(self):
        return f"{self.author} - {self.header}"   

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, verbose_name="Автор", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Содержание")
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    
    def __str__(self):
        return f"{self.author} - {self.post}"
    
    def __repr__(self):
        return f"{self.author} - {self.post}"   

class Check(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    total = models.FloatField(verbose_name="Итого")
    date = models.DateTimeField(verbose_name="Дата и время", default=now)
    
    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"
        
    def __str__(self):
        return f"{self.user} - {self.date} - {self.total}"
    
    def __repr__(self):
        return f"{self.user} - {self.date} - {self.total}" 

class Review(Post):
    rating = models.IntegerField(verbose_name="Оценка")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        
    def __str__(self):
        return f"{self.rating} - {self.author} - {self.product}"
    
    def __repr__(self):
        return f"{self.rating} - {self.author} - {self.product}"

class Library(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    cdkey = models.ForeignKey(CDKey, on_delete=models.CASCADE, verbose_name="Ключ")
    
    class Meta:
        verbose_name = "Игра пользователя"
        verbose_name_plural = "Библиотека"
        
    def __str__(self):
        return f"{self.user} - {self.product} - {self.cdkey}"
    
    def __repr__(self):
        return f"{self.user} - {self.product} - {self.cdkey}"