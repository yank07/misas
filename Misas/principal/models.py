from django.db import models

# Create your models here.
class Ciudad(models.Model):    
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.nombre)
class Horario(models.Model):
    hora = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.hora)
    
class Iglesia(models.Model):
    
    nombre = models.CharField(max_length=50)
    parrocos = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, related_name='iglesias')
    direccion = models.CharField(max_length=140)
    ubicacion = models.URLField()
    horarios_misa = models.ManyToManyField(HorarioMisa)
    horarios_confesion = models.ManyToManyField(HorarioConfesion)
    coord_long = models.FloatField()
    coord_lat = models.FloatField()
      
    
    def __unicode__(self):
        return unicode(self.nombre)
    
    
