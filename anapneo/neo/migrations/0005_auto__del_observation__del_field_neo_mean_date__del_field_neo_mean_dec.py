# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Observation'
        db.delete_table(u'neo_observation')

        # Deleting field 'Neo.mean_date'
        db.delete_column(u'neo_neo', 'mean_date')

        # Deleting field 'Neo.mean_dec'
        db.delete_column(u'neo_neo', 'mean_dec')

        # Deleting field 'Neo.mean_ra'
        db.delete_column(u'neo_neo', 'mean_ra')

        # Adding field 'Neo.user'
        db.add_column(u'neo_neo', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Neo.score'
        db.add_column(u'neo_neo', 'score',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Neo.observation_date'
        db.add_column(u'neo_neo', 'observation_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 21, 0, 0)),
                      keep_default=False)

        # Adding field 'Neo.position_ra'
        db.add_column(u'neo_neo', 'position_ra',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Neo.position_dec'
        db.add_column(u'neo_neo', 'position_dec',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Neo.magnitude'
        db.add_column(u'neo_neo', 'magnitude',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Neo.updated'
        db.add_column(u'neo_neo', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 21, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'Neo.note'
        db.add_column(u'neo_neo', 'note',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Neo.num_obs'
        db.add_column(u'neo_neo', 'num_obs',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Neo.arc'
        db.add_column(u'neo_neo', 'arc',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Neo.nominal_h'
        db.add_column(u'neo_neo', 'nominal_h',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Removing M2M table for field obsrv_range on 'Neo'
        db.delete_table('neo_neo_obsrv_range')


    def backwards(self, orm):
        # Adding model 'Observation'
        db.create_table(u'neo_observation', (
            ('position_dec', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telescope', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('magnitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('observation_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exposure', self.gf('django.db.models.fields.FloatField')()),
            ('position_ra', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('instrument', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('aperture', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'neo', ['Observation'])


        # User chose to not deal with backwards NULL issues for 'Neo.mean_date'
        raise RuntimeError("Cannot reverse this migration. 'Neo.mean_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Neo.mean_dec'
        raise RuntimeError("Cannot reverse this migration. 'Neo.mean_dec' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Neo.mean_ra'
        raise RuntimeError("Cannot reverse this migration. 'Neo.mean_ra' and its values cannot be restored.")
        # Deleting field 'Neo.user'
        db.delete_column(u'neo_neo', 'user_id')

        # Deleting field 'Neo.score'
        db.delete_column(u'neo_neo', 'score')

        # Deleting field 'Neo.observation_date'
        db.delete_column(u'neo_neo', 'observation_date')

        # Deleting field 'Neo.position_ra'
        db.delete_column(u'neo_neo', 'position_ra')

        # Deleting field 'Neo.position_dec'
        db.delete_column(u'neo_neo', 'position_dec')

        # Deleting field 'Neo.magnitude'
        db.delete_column(u'neo_neo', 'magnitude')

        # Deleting field 'Neo.updated'
        db.delete_column(u'neo_neo', 'updated')

        # Deleting field 'Neo.note'
        db.delete_column(u'neo_neo', 'note')

        # Deleting field 'Neo.num_obs'
        db.delete_column(u'neo_neo', 'num_obs')

        # Deleting field 'Neo.arc'
        db.delete_column(u'neo_neo', 'arc')

        # Deleting field 'Neo.nominal_h'
        db.delete_column(u'neo_neo', 'nominal_h')

        # Adding M2M table for field obsrv_range on 'Neo'
        db.create_table(u'neo_neo_obsrv_range', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('neo', models.ForeignKey(orm[u'neo.neo'], null=False)),
            ('observation', models.ForeignKey(orm[u'neo.observation'], null=False))
        ))
        db.create_unique(u'neo_neo_obsrv_range', ['neo_id', 'observation_id'])


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
            'arc': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'magnitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nominal_h': ('django.db.models.fields.FloatField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'num_obs': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'observation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'position_dec': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position_ra': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'max_length': '100'}),
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