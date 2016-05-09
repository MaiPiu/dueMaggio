from django.db import models
class Pizza(models.Model):
    nome = models.CharField(max_length=200)
    descrcizione = models.CharField(max_length=200)
    fotoUrl = models.CharField(max_length=200)
    class Meta:
	    verbose_name_plural = "Pizze"
    def __unicode__(self):
	    return u"%s" % (self.nome)
	    
class Farina(models.Model):
    tipo = models.CharField(max_length=200)
    class Meta:
	    verbose_name_plural = "Farine"
    def __unicode__(self):
	    return u"%s" % (self.tipo)
    
class Ordine(models.Model):
    cliente = models.CharField(max_length=200)
    indirizzoConsegna = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    eMail = models.CharField(max_length=200)
    dataOrdine = models.DateTimeField('date published')
    class Meta:
	    verbose_name_plural = "Ordini"
    def __unicode__(self):
	    return u"%s" % (self.id)
    
class Dettaglio(models.Model):
    noPizze = models.CharField(max_length=200)
    ingredientiAggiuntivi = models.CharField(max_length=200)
    pizza_fk = models.ForeignKey(Pizza)
    farina_fk = models.ForeignKey(Farina)
    ordine_fk = models.ForeignKey(Ordine)
    class Meta:
	    verbose_name_plural = "Dettagli"
    def __unicode__(self):
	    return u"%s" % (self.noPizze)