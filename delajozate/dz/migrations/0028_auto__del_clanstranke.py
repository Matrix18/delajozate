# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ClanStranke'
        db.delete_table('dz_clanstranke')


    def backwards(self, orm):
        
        # Adding model 'ClanStranke'
        db.create_table('dz_clanstranke', (
            ('do', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('opombe', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('stranka', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dz.Stranka'], null=True, blank=True)),
            ('podatki_preverjeni', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oseba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dz.Oseba'])),
            ('od', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dz', ['ClanStranke'])


    models = {
        'dz.clanodbora': {
            'Meta': {'object_name': 'ClanOdbora'},
            'do': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'funkcija': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mandat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Mandat']"}),
            'od': ('django.db.models.fields.DateField', [], {}),
            'odbor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.DelovnoTelo']"}),
            'opombe': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'podatki_preverjeni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'poslanec': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Funkcija']"})
        },
        'dz.delovnotelo': {
            'Meta': {'object_name': 'DelovnoTelo'},
            'do': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'dz_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ime': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'mandat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Mandat']"}),
            'od': ('django.db.models.fields.DateField', [], {}),
            'opombe': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizacija': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dz.Organizacija']", 'unique': 'True', 'null': 'True'}),
            'podatki_preverjeni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'dz.drzavnizbor': {
            'Meta': {'object_name': 'DrzavniZbor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mandat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Mandat']"}),
            'organizacija': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dz.Organizacija']", 'unique': 'True', 'null': 'True'})
        },
        'dz.funkcija': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Funkcija'},
            'do': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'funkcija': ('django.db.models.fields.CharField', [], {'default': "'poslanec'", 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mandat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Mandat']"}),
            'od': ('django.db.models.fields.DateField', [], {}),
            'opombe': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oseba': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Oseba']"}),
            'podatki_preverjeni': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dz.imestranke': {
            'Meta': {'ordering': "['-od']", 'object_name': 'ImeStranke'},
            'do': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(9999, 12, 31)', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ime': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'od': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'stranka': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Stranka']"})
        },
        'dz.mandat': {
            'Meta': {'object_name': 'Mandat'},
            'do': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(9999, 12, 31)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'od': ('django.db.models.fields.DateField', [], {}),
            'st': ('django.db.models.fields.IntegerField', [], {})
        },
        'dz.organizacija': {
            'Meta': {'object_name': 'Organizacija'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tip': ('django.db.models.fields.IntegerField', [], {})
        },
        'dz.oseba': {
            'Meta': {'ordering': "('priimek', 'ime')", 'object_name': 'Oseba'},
            'dan_smrti': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '64', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ime': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'opombe': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'podatki_preverjeni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'priimek': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'rojstni_dan': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slika': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '96', 'db_index': 'True'}),
            'spletna_stran': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'vir_slike': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'dz.pozicija': {
            'Meta': {'object_name': 'Pozicija'},
            'do': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(9999, 12, 31)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'od': ('django.db.models.fields.DateField', [], {}),
            'opombe': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizacija': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Organizacija']", 'null': 'True'}),
            'oseba': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Oseba']"}),
            'podatki_preverjeni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tip': ('django.db.models.fields.CharField', [], {'default': "'poslanec'", 'max_length': '64'})
        },
        'dz.skupina': {
            'Meta': {'object_name': 'Skupina'},
            'do': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ime': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'mandat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Mandat']"}),
            'od': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'organizacija': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dz.Organizacija']", 'unique': 'True', 'null': 'True'}),
            'stranka': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Stranka']", 'null': 'True', 'blank': 'True'})
        },
        'dz.stranka': {
            'Meta': {'ordering': "('-do', 'ime')", 'object_name': 'Stranka'},
            'barva': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'davcna': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'do': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(9999, 12, 31)', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '64', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ime': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'maticna': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'nastala_iz': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'spremenila_v'", 'blank': 'True', 'to': "orm['dz.Stranka']"}),
            'od': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'okrajsava': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'opombe': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizacija': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dz.Organizacija']", 'unique': 'True', 'null': 'True'}),
            'podatki_preverjeni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spletna_stran': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        'dz.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oseba': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dz.Oseba']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tweet_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['dz']
