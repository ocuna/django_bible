from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from bible_api.models import BRBverses

@admin.register(BRBverses)
class BRBversesAdmin(ImportExportModelAdmin):
	list_display = ('bcvCode','book','verseNumber','chaperNumber','verse')
	pass

# Register your models here.
