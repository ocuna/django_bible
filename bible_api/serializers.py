from rest_framework import serializers
from . models import BRB_Verses

class BRB_Verses_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		verbose_name = 'BRB Verses'
		verbose_name_plural = 'BRB Verses'
		model = BRB_Verses
		fields = ('id','url','book','chapterNumber','verseNumber','verse')