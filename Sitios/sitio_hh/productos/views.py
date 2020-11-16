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

        if not (len(groups) == 1 and groups[0] == ""):
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
            query = query.filter(categoria__title__iexact=categoriaFiltro)
        
        if len(wordsFiltro) > 0:
            query_original = query
            query = query_original.filter(name__icontains=wordsFiltro[0])
            for word in wordsFiltro:
                query = query | query_original.filter(name__icontains=word)
            


        list_categorias = Categoria.objects.all()
        list_productos = query
    else:
        list_categorias = Categoria.objects.all()
        list_productos = Producto.objects.all()

    return render(request, "productos/search.html", {'list_categorias':list_categorias, 'list_productos':list_productos})  