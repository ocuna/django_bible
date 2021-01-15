import textwrap
from django.db import models

class BRB_Verses(models.Model):
	bcvCode = models.CharField(max_length=25, default='')
	book = models.CharField(max_length=25, default='')
	bookAbr = models.CharField(max_length=3, default='')
	verseSumNumber = models.IntegerField(default=0)
	verseNumber = models.IntegerField(default=0)
	chapterNumber = models.IntegerField(default=0)
	verse = models.TextField(default='')

	class Meta:
		db_table = "BRB"
		verbose_name = 'BRB Verses'
		verbose_name_plural = 'BRB Verses'
		ordering = ['verseSumNumber']

	def __str__(self):	
		prefix = str(self.verseSumNumber) + " | " + self.book + " " + str(self.chapterNumber) + ":" + str(self.verseNumber)
		suffix = textwrap.shorten(self.verse, width=100, placeholder="...")
		return prefix + " | " + suffix   

