from django.shortcuts import render_to_response
from models import Book
def busqueda_form(request):
	return render_to_response('busqueda_form.html')

def search(request):
	query=request.GET.get('q','')
	if query:
		qset=(
			Q(title__icontains=query)
			#Q(autores__first_name__icontains=query)
			#Q(autores__last_name__icontains=query)

		)
		results=Book.object.filter(qset).distinct()
	else:
		results=[]
		return render_to_response("busqueda_form.html",{
			"results":results,
			"query":query
		})