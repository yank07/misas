# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ciudad'
        db.create_table(u'principal_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'principal', ['Ciudad'])

        # Adding model 'Horario'
        db.create_table(u'principal_horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'principal', ['Horario'])

        # Adding model 'Iglesia'
        db.create_table(u'principal_iglesia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parrocos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='iglesias', to=orm['principal.Ciudad'])),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('ubicacion', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('coord_long', self.gf('django.db.models.fields.FloatField')()),
            ('coord_lat', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'principal', ['Iglesia'])

        # Adding M2M table for field horarios on 'Iglesia'
        m2m_table_name = db.shorten_name(u'principal_iglesia_horarios')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iglesia', models.ForeignKey(orm[u'principal.iglesia'], null=False)),
            ('horario', models.ForeignKey(orm[u'principal.horario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['iglesia_id', 'horario_id'])


    def backwards(self, orm):
        # Deleting model 'Ciudad'
        db.delete_table(u'principal_ciudad')

        # Deleting model 'Horario'
        db.delete_table(u'principal_horario')

        # Deleting model 'Iglesia'
        db.delete_table(u'principal_iglesia')

        # Removing M2M table for field horarios on 'Iglesia'
        db.delete_table(db.shorten_name(u'principal_iglesia_horarios'))


    models = {
        u'principal.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'principal.horario': {
            'Meta': {'object_name': 'Horario'},
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.iglesia': {
            'Meta': {'object_name': 'Iglesia'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'iglesias'", 'to': u"orm['principal.Ciudad']"}),
            'coord_lat': ('django.db.models.fields.FloatField', [], {}),
            'coord_long': ('django.db.models.fields.FloatField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'horarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['principal.Horario']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parrocos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ubicacion': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['principal']