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

        # Adding model 'HorarioMisa'
        db.create_table(u'principal_horariomisa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'principal', ['HorarioMisa'])

        # Adding model 'HorarioConfesion'
        db.create_table(u'principal_horarioconfesion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'principal', ['HorarioConfesion'])

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

        # Adding M2M table for field horarios_misa on 'Iglesia'
        m2m_table_name = db.shorten_name(u'principal_iglesia_horarios_misa')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iglesia', models.ForeignKey(orm[u'principal.iglesia'], null=False)),
            ('horariomisa', models.ForeignKey(orm[u'principal.horariomisa'], null=False))
        ))
        db.create_unique(m2m_table_name, ['iglesia_id', 'horariomisa_id'])

        # Adding M2M table for field horarios_confesion on 'Iglesia'
        m2m_table_name = db.shorten_name(u'principal_iglesia_horarios_confesion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iglesia', models.ForeignKey(orm[u'principal.iglesia'], null=False)),
            ('horarioconfesion', models.ForeignKey(orm[u'principal.horarioconfesion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['iglesia_id', 'horarioconfesion_id'])

        # Adding model 'Fruit'
        db.create_table(u'principal_fruit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('peso', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'principal', ['Fruit'])


    def backwards(self, orm):
        # Deleting model 'Ciudad'
        db.delete_table(u'principal_ciudad')

        # Deleting model 'HorarioMisa'
        db.delete_table(u'principal_horariomisa')

        # Deleting model 'HorarioConfesion'
        db.delete_table(u'principal_horarioconfesion')

        # Deleting model 'Iglesia'
        db.delete_table(u'principal_iglesia')

        # Removing M2M table for field horarios_misa on 'Iglesia'
        db.delete_table(db.shorten_name(u'principal_iglesia_horarios_misa'))

        # Removing M2M table for field horarios_confesion on 'Iglesia'
        db.delete_table(db.shorten_name(u'principal_iglesia_horarios_confesion'))

        # Deleting model 'Fruit'
        db.delete_table(u'principal_fruit')


    models = {
        u'principal.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'principal.fruit': {
            'Meta': {'object_name': 'Fruit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'peso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'principal.horarioconfesion': {
            'Meta': {'object_name': 'HorarioConfesion'},
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.horariomisa': {
            'Meta': {'object_name': 'HorarioMisa'},
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.iglesia': {
            'Meta': {'object_name': 'Iglesia'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'iglesias'", 'to': u"orm['principal.Ciudad']"}),
            'coord_lat': ('django.db.models.fields.FloatField', [], {}),
            'coord_long': ('django.db.models.fields.FloatField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'horarios_confesion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['principal.HorarioConfesion']", 'symmetrical': 'False'}),
            'horarios_misa': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['principal.HorarioMisa']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parrocos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ubicacion': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['principal']