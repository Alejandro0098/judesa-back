from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(null=False, unique=True, max_length=150)
    subtitle =  models.CharField(null=False, unique=True, max_length=150)
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    preview_image =  models.CharField(null=False, max_length=150)
    tags = models.JSONField()

    class Meta:
        db_table = 'News'

    def __str__(self):
        return f'New {self.id} - {self.creation_date.date()}'
    
    def _to_json(self):
        return {
            "new": {
                "id": self.id,
                "title": self.title,
                "subtitle": self.subtitle,
                "creation_date": self.creation_date.date(),
                "image": self.preview_image,
            },
            "tags": self.tags['tags']
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

    def __str__(self):
        return f'{self.id}. Sponsor {self.name} - {'Activo' if self.is_active else 'Inactivo'}'
    
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

    def __str__(self):
        return f'{self.id}. {self.name} category'
    
    def _to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "trainer": self.trainer._to_json() if self.trainer else {},
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
    category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, related_name='category_id_matches', null=True)
    location = models.CharField(null=False, unique=True, max_length=150, default='')
    rival = models.CharField(null=False, max_length=150)
    local_score = models.PositiveIntegerField(default=0)
    visitant_score = models.PositiveIntegerField(default=0)
    match_date = models.DateTimeField(null=False)
    is_local = models.BooleanField(default=True)
    show_result = models.BooleanField(default=False)

    class Meta:
        db_table = 'Matches'

    def __str__(self):
        match = self._to_json()
        local = match.get('local')
        visitant = match.get('visitant')
        
        return f'{self.id}. {local.get('name')} vs {visitant.get('name')} {f'{local.get('score')} - {visitant.get('score')}' if self.show_result else ''}'
    
    def _to_json(self):
        
        judesa_name = 'CD Judesa FS' 
        
        return {
            "id": self.id,
            "local": {
                "name": judesa_name if self.is_local else self.rival,
                "score": self.local_score
            },
            "visitant": {
                "name": judesa_name if not self.is_local else self.rival,
                "score": self.visitant_score
            }, 
            "match_date": {
                "extended": self.match_date,
                "date": self.match_date.date(),
                    "time": f'{self.match_date.time().hour}:{f'0{self.match_date.time().minute}' if self.match_date.time().minute < 10 else self.match_date.time().minute}' 
            },
            "show_result": self.show_result,
            "is_local": self.is_local,
            "location": self.location
        }