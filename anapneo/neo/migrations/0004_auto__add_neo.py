# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Neo'
        db.create_table(u'neo_neo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mean_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('mean_ra', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mean_dec', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'neo', ['Neo'])

        # Adding M2M table for field obsrv_range on 'Neo'
        db.create_table(u'neo_neo_obsrv_range', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('neo', models.ForeignKey(orm[u'neo.neo'], null=False)),
            ('observation', models.ForeignKey(orm[u'neo.observation'], null=False))
        ))
        db.create_unique(u'neo_neo_obsrv_range', ['neo_id', 'observation_id'])


    def backwards(self, orm):
        # Deleting model 'Neo'
        db.delete_table(u'neo_neo')

        # Removing M2M table for field obsrv_range on 'Neo'
        db.delete_table('neo_neo_obsrv_range')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'neo.neo': {
            'Meta': {'object_name': 'Neo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mean_date': ('django.db.models.fields.DateTimeField', [], {}),
            'mean_dec': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mean_ra': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'obsrv_range': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['neo.Observation']", 'symmetrical': 'False'})
        },
        u'neo.observation': {
            'Meta': {'object_name': 'Observation'},
            'aperture': ('django.db.models.fields.FloatField', [], {}),
            'exposure': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'magnitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'observation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'position_dec': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position_ra': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telescope': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'neo.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '40'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '40'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '100'}),
            'lat': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '20'}),
            'lon': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['neo']