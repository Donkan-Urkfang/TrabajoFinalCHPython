from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Juego(models.Model):
    plataformas = [
        ('Playstation 5','Playstation 5'),
        ('Xbox Series X/S','Xbox Series X/S'),
        ('Nintendo Switch', 'Nintendo Switch'),
        ('PC', 'PC'),
        ('Xbox 360', 'Xbox 360'),
        ('Nintendo DS','Nintendo DS') ,
        ('Playstation 4', 'Playstation 4'),
        ('Playstation 3', 'Playstation 3'),
        ('Playstation 2', 'Playstation 2'),
        ('Playstation', 'Playstation'),
        ('Gameboy Advance', 'Gameboy Advance'),
        ('Gameboy', 'Gameboy'),
        ('Xbox', 'Xbox'),
        ('Xbox One', 'Xbox One'),
        ('Nintendo', 'Nintendo'),
        ('Super Nintendo', 'Super Nintendo'),
        ('Nintendo Wii', 'Nintendo Wii'),
        ('Nintendo 64', 'Nintendo 64'),
        ('Megadrive', 'Megadrive'),
        ('Nintendo Wii U', 'Nintendo Wii U'),
        ]

    nombre = models.CharField("nombre", max_length=50)
    genero = models.CharField("genero", max_length=50)
    fechaDeLanzamiento = models.DateField("fechaDeLanzamiento", auto_now=False, auto_now_add=False)
    plataforma = models.CharField("plataforma", max_length=50, choices=plataformas, null=True, blank=True)
    imagen = models.ImageField(upload_to= 'avatares', null=True, blank=True)


    def __str__(self):
        return f'{self.nombre} - Genero: {self.genero} - Año de Lanzamiento: {self.fechaDeLanzamiento} - Plataforma: {self.plataforma} - Imagen {self.imagen}'

class Desarrolladora(models.Model):
    nombre= models.CharField(max_length=50)
    pais= models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    contacto = models.EmailField(max_length=254, blank=True)
    imagen = models.ImageField(upload_to= 'avatares', null=True, blank=True)

    
    def __str__(self):
        return f'Nombre: {self.nombre} - Pais: {self.pais} - Ciudad: {self.ciudad} - Contacto: {self.contacto} - Imagen {self.imagen}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= 'avatares', null=True, blank=True)

    def __str__(self):
        return f'Imagen de {self.user.username} '

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'