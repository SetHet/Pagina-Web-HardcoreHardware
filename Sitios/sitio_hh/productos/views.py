from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
def search(request):

    if (request.method == 'GET'):

        search = request.GET
        print(search)

        groups = search['search'].split(' ')
        print(groups)

        categoriaFiltro = ""
        wordsFiltro = []

        for grp in groups:
            comandos = grp.split(':')
            if len(comandos) > 1:
                print(comandos[0])
                if comandos[0].lower() == "categoria":
                    categoriaFiltro = comandos[1]
                    continue
            wordsFiltro.append(comandos[0])

        print("cat > " + categoriaFiltro)
        print("words > " + str(wordsFiltro))

        query = Producto.objects.all()
        if categoriaFiltro != "":
            query = query.filter(categoria__iexact=categoriaFiltro)
        
        query_original = query

        for word in wordsFiltro:
            query = query | query_original.filter()

        list_categorias = Categoria.objects.all()
        list_productos = query
    else:
        list_categorias = Categoria.objects.all()
        list_productos = Producto.objects.all()

    return render(request, "productos/search.html", {'list_categorias':list_categorias, 'list_productos':list_productos})  