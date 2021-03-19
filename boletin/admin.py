from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	  list_display = ["email","nombre","timestamp"]
	  form = RegModelForm
	  list_filter= ["nombre", "email"]
	  list_editable =["nombre"]
	  search_fidels= ["email", "nombre"]

	  # class Meta:
	  #	model= Registrado

admin.site.register(Registrado,AdminRegistrado)
