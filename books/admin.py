from django.contrib import admin
from books.models import Editor, Autor, Book

class AutorAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','email' )
	search_fields=('first_name','last_name')

class BooksAdmin(admin.ModelAdmin):
	list_display=('title','editor','publicatio_date')
	list_filter=('publicatio_date',)
#Ordena los campos 
	fields=('title','autores','editor','publicatio_date')
	filter_horizontal=('autores',)
	raw_id_fields=('editor',)


admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Book, BooksAdmin)