# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.name'
        db.delete_column(u'persons_person', 'name')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Person.name'
        raise RuntimeError("Cannot reverse this migration. 'Person.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Person.name'
        db.add_column(u'persons_person', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=256),
                      keep_default=False)


    models = {
        u'persons.person': {
            'Meta': {'object_name': 'Person'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'created_at_turn': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "u'{}'"}),
            'enemies_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'friends_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('rels.django.RelationIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_forms': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'out_game_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persons'", 'on_delete': 'models.PROTECT', 'to': u"orm['places.Place']"}),
            'race': ('rels.django.RelationIntegerField', [], {}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('rels.django.RelationIntegerField', [], {})
        },
        u'places.place': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Place'},
            'data': ('django.db.models.fields.TextField', [], {'default': "u'{}'"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'expected_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'freedom': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'goods': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'heroes_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('rels.django.RelationIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'}),
            'name_forms': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'persons_changed_at_turn': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'production': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'race': ('rels.django.RelationIntegerField', [], {}),
            'safety': ('django.db.models.fields.FloatField', [], {'default': '0.75'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'transport': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_at_turn': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'x': ('django.db.models.fields.BigIntegerField', [], {}),
            'y': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['persons']