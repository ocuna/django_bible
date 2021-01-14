from rest_framework import serializers
from . models import BRB_Verses

class BRB_Verses_Serializer(serializers.ModelSerializer):
	class Meta:
		model = BRB_Verses
		fields = ('book','chapterNumber','verseNumber','verse')