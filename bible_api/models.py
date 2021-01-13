from django.db import models

class BRBverses(models.Model):
	bcvCode = models.CharField(max_length=25)
	book = models.CharField(max_length=25)
	verseNumber = models.IntegerField()
	chaperNumber = models.IntegerField()
	verse = models.TextField()

	class Meta:
		db_table = "BRB"