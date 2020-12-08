from .models import Categoria

def ctx_dict(request):

    categorias = Categoria.objects.all().order_by('nameSpanish')

    ctx = {'lista_categorias':categorias}

    return ctx