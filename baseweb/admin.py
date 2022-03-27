from baseweb.models import Empresa
from django.contrib import admin
from .models import Empresa #ahi se importa la tabla
# Register your models here.

admin.site.register(Empresa)