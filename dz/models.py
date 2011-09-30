# coding: utf-8
from django.db import models
from django.template.defaultfilters import slugify
from delajozate.temporal import END_OF_TIME

class Oseba(models.Model):
	ime = models.CharField(max_length=32)
	priimek = models.CharField(max_length=64)
	slug = models.SlugField(max_length=96)
	email = models.EmailField(max_length=64, blank=True)
	rojstni_dan = models.DateField(blank=True, null=True)
	slika = models.CharField(max_length=200, blank=True)
	spletna_stran = models.URLField(blank=True)
	twitter = models.CharField(max_length=32, blank=True)
	facebook = models.URLField(blank=True)
	
	class Meta:
		ordering = ('ime', 'priimek')
		verbose_name_plural = u'Osebe'
	
	def __unicode__(self):
		return u'%s %s' % (self.ime, self.priimek)
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slug = slugify("%s %s" % (self.ime, self.priimek))
			count = 2
			while Oseba.objects.filter(slug=self.slug).count():
				self.slug = "%s-%d" % (slug, count)
				count += 1
				
		super(Oseba, self).save(*args, **kwargs)


class Stranka(models.Model):
	# kako modelirat kontinuiteto stranke, kadar se preimenuje?
	#parent_stranka = models.IntegerField(null=True)
	ime = models.CharField(max_length=64)
	maticna = models.CharField(max_length=10, blank=True)
	davcna = models.CharField(max_length=10, blank=True)
	okrajsava = models.CharField(max_length=16)
	email = models.EmailField(max_length=64, blank=True)
	barva = models.CharField(max_length=6)
	od = models.DateField()
	do = models.DateField(default=END_OF_TIME)
	spletna_stran = models.URLField(blank=True)
	twitter = models.CharField(max_length=32, blank=True)
	facebook = models.URLField(blank=True)
	opombe = models.TextField(blank=True)
	
	class Meta:
		verbose_name_plural = u'Stranke'
	
	def __unicode__(self):
		return u'%s (%s)%s' % (self.ime, self.okrajsava, self.do != END_OF_TIME and u'\u271d' or u'')

class Skupina(models.Model): # Poslanska
	ime = models.CharField(max_length=64)
	stranka = models.ForeignKey(Stranka, null=True, blank=True)
	
	class Meta:
		verbose_name_plural = u'Skupine'


class ClanStranke(models.Model):
	oseba = models.ForeignKey(Oseba)
	od = models.DateField()
	do = models.DateField(blank=True)
	
	class Meta:
		verbose_name = u'Član stranke'
		verbose_name_plural = u'Člani strank'


class Mandat(models.Model):
	st = models.IntegerField() # Kateri mandat
	od = models.DateField()
	do = models.DateField(blank=True, default=END_OF_TIME)
	
	class Meta:
		verbose_name_plural = u'Mandati'
	
	def __unicode__(self):
		return unicode(self.st)

class Poslanec(models.Model):
	oseba = models.ForeignKey(Oseba)
	mandat = models.ForeignKey(Mandat)
	od = models.DateField()
	do = models.DateField(blank=True)
	
	class Meta:
		verbose_name_plural = u'Poslanci'
	
	def __unicode__(self):
		return u'%s (%s)' % (self.oseba, self.mandat)


class Odbor(models.Model):
	ime = models.CharField(max_length=64)
	mandat = models.ForeignKey(Mandat)
	od = models.DateField()
	do = models.DateField(blank=True)
	
	class Meta:
		verbose_name_plural = u'Odbori'


class ClanOdbora(models.Model):
	odbor = models.ForeignKey(Odbor)
	poslanec = models.ForeignKey(Poslanec)
	mandat = models.ForeignKey(Mandat)
	funkcija = models.CharField(max_length=32)
	od = models.DateField()
	do = models.DateField(blank=True)
	
	class Meta:
		verbose_name = u'Član odbora'
		verbose_name_plural = u'Člani odbora'
	
