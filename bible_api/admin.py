from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from bible_api.models import BRB_Verses

@admin.register(BRB_Verses)
class BRB_VersesAdmin(ImportExportModelAdmin):
	list_display = ('bcvCode','book','verseNumber','chapterNumber','verse')
	pass

# Register your models here.
