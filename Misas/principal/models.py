from django.db import models

# Create your models here.

class Pais(models.Model):    
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.nombre)
class Ciudad(models.Model):    
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.nombre)
class Barrio(models.Model):    
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.nombre)
class HorarioMisa(models.Model):
    hora = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.hora)
class HorarioConfesion(models.Model):
    hora = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.hora)
    
class Iglesia(models.Model):
    
    nombre = models.CharField(max_length=50)
    parrocos = models.CharField(max_length=100)
    pais =  models.ForeignKey(Pais, related_name='iglesias', default='')
    ciudad = models.ForeignKey(Ciudad, related_name='iglesias', default='')
    barrio = models.ForeignKey(Barrio, related_name='iglesias', default='')
    direccion = models.CharField(max_length=140)
    ubicacion = models.URLField()
    telefono = models.CharField(max_length=30)
    horarios_misa = models.ManyToManyField(HorarioMisa)
    horarios_confesion = models.ManyToManyField(HorarioConfesion)
    coord_long = models.FloatField()
    coord_lat = models.FloatField()      
    
    def __unicode__(self):
        return unicode(self.nombre)

class Fruit(models.Model):
    name = models.CharField(max_length=200)
    peso = models.IntegerField()

    def __unicode__(self):
        return self.name
    
