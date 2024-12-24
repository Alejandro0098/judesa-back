from django.db import models
from django.contrib import admin

class News(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(null=False, unique=True, max_length=150)
    subtitle =  models.CharField(null=False, unique=True, max_length=150)
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    preview_image =  models.CharField(null=False, max_length=150)
    tags = models.JSONField()

    class Meta:
        db_table = 'News'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return f'Noticia {self.id} - {self.creation_date.date().strftime('%d/%m/%Y')}'
    
    def _to_json(self):
        return {
            "new": {
                "id": self.id,
                "title": self.title,
                "subtitle": self.subtitle,
                "creation_date": self.creation_date.date().strftime('%d/%m/%Y'),
                "image": self.preview_image,
            },
            "tags": self.tags
        }
        

class Sponsors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, unique=True, max_length=150)
    description = models.CharField(null=False, unique=True, max_length=150)
    image = models.CharField(null=False, unique=True, max_length=150)
    social = models.JSONField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Sponsors'
        verbose_name_plural = 'Patrocinadores'

    def __str__(self):
        if self.is_active:
            active = 'Activo'
        else:
            active = 'Inactivo'
        
        return f'{self.id}. Patrocinador {self.name} - {active}'
    
    def _to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "social": self.social
            }


class Products(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, unique=True, max_length=150)
    description = models.CharField(null=False, unique=True, max_length=150)
    prize = models.CharField(null=False, unique=True, max_length=150)
    is_active = models.CharField(null=False, unique=True, max_length=150)
    creation_date = models.CharField(null=False, unique=True, max_length=150)
    image = models.CharField(null=False, unique=True, max_length=150)

    class Meta:
        db_table = 'Products'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.id}. {self.name}'


class Staff(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, unique=True, max_length=150)
    creation_date =  models.DateTimeField(null=False, auto_now_add=True)
    image = models.CharField(default='', max_length=150)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return f'{self.id}. {self.name}'
    
    def _to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "creation_date": self.creation_date.date(),
            "is_active": self.is_active,
            "image": self.image
        }


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    trainer = models.ForeignKey(Staff, on_delete=models.SET_NULL, related_name='trainer_id', null=True)
    delegate = models.ForeignKey(Staff, on_delete=models.SET_NULL, related_name='delegate_id', null=True)
    name = models.CharField(null=False, unique=True, max_length=150)
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    image = models.CharField(default='', max_length=150)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'Categories'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return f'Categoría {self.name}'
    
    def _to_json(self): 
        return {
            "id": self.id,
            "name": self.name,
            "trainer": self.trainer._to_json(),
            "delegate": self.delegate._to_json() if self.delegate else {},
            "image": self.image
        }
        
        
class Players(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, related_name='category_id_players', null=True)
    name = models.CharField(null=False, unique=True, max_length=150)
    last_name = models.CharField(null=False, unique=True, max_length=150)
    alias = models.CharField(null=False, unique=True, max_length=150)
    position = models.CharField(null=False, unique=True, max_length=150)
    dorsal = models.IntegerField(null=False, unique=True)
    birthday_date = models.DateField()
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    image = models.CharField(null=False, unique=True, max_length=150)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Players'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return f'{self.id}. {self.name} - #{self.dorsal}'
    
    def _to_json(self):
        return {
            "id": self.id,   
            "name": self.name,
            "last_name": self.last_name,
            "alias": self.alias,
            "position": self.position,
            "dorsal": self.dorsal,
            "image": self.image,
        }


class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, related_name='category_id_matches', null=True, verbose_name='categoría')
    location = models.CharField(null=False, unique=True, max_length=150, default='')
    rival = models.CharField(null=False, max_length=150)
    local_score = models.PositiveIntegerField(default=0)
    visitant_score = models.PositiveIntegerField(default=0)
    match_date = models.DateTimeField(null=False, verbose_name="fecha")
    is_local = models.BooleanField(default=True)
    show_result = models.BooleanField(default=False)

    class Meta:
        db_table = 'Matches'
        verbose_name_plural = 'Partidos'
        verbose_name = 'Partido'
        

    def __str__(self):

        result = f'vs {self.rival}'

        if self.show_result:
            result += f' --> {self.local_score} - {self.visitant_score}'
        
        return result
    
    def _to_json(self):

        time = f'{self.match_date.time().hour}:'
        if self.match_date.time().minute > 10:
            time += str(self.match_date.time().minute)
        else:
            time += '0' + str(self.match_date.time().minute)
            
        return {
            "id": self.id,
            "category": self.category_id.name,
            "date": self.match_date.date().strftime('%d/%m/%Y'),
            "time": time,
            "rival": self.rival,
            "result": str(self.local_score) + '-' + str(self.visitant_score),
            "show_result": self.show_result,
            "is_local": self.is_local,
            "location": self.location
         }