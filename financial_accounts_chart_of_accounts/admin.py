from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ClientCategory)
admin.site.register(Ledger)
admin.site.register(Journal)
admin.site.register(JournalEntry)