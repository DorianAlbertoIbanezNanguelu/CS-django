from django.db import models
from django.utils import timezone 

# Create your models here.

class CiudadModel(models.Model):
    
    ciudad = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now) 

    class Meta:
        db_table = 'Ciudad'

    def __str__(self):
        return self.ciudad
    
class GeneroModel(models.Model):
    
    genero = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now) 

    class Meta:
        db_table = 'Genero'

    def __str__(self):
        return self.genero

class OcupacionModel(models.Model):
    
    ocupacion = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now) 

    class Meta:
        db_table = 'Ocupacion'
    
    def __str__(self):
        return self.ocupacion

class EstadoModel(models.Model):

    estado = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now) 

    class Meta:
        db_table = 'Estado'
    
    def __str__(self):
        return self.estado

class EstadoCivilModel(models.Model):

    estado_civil = models.CharField(max_length=254,null=False) 
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now) 

    class Meta:
        db_table = 'EstadoCivil'
    
    def __str__(self):
        return self.estado_civil

class ProfileModel(models.Model):

    nombre = models.CharField(max_length=254,null=False)
    apPat = models.CharField(max_length=254,null=False)
    apMat = models.CharField(max_length=254,null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(CiudadModel,on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroModel,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(OcupacionModel,on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoModel,on_delete=models.CASCADE)
    estadoCivil = models.ForeignKey(EstadoCivilModel,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)    

    class Meta:
        db_table = 'Profile'
