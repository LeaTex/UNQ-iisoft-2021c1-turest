from administracion.models import Item

class Cart():
    def __init__(self, request):
        if not 'pedidos' in request.session:
            request.session['pedidos'] = []
            request.session['pedidos_id'] = 0
        self.session = request.session
        self.request = request

    def newId(self):
        self.session['pedidos_id'] = self.session['pedidos_id']+1
        return self.session['pedidos_id']-1

    def limpiar(self):
        print("borramos pedidos")
        del self.session['pedidos']

    def registrar(self):
        self.limpiar()

    def agregarPedido(self):
        id = self.newId()
        pedido = (id, self.request.POST['item'], self.request.POST['cantidad'])
        list = self.session['pedidos']
        list.append(pedido)
        self.session['pedidos'] = list

    def getItems(self):
        lista = []
        self.precioTotal = 0
        for id, itemId, cantidad in self.session.get('pedidos', []):
            item = Item.objects.get(pk=int(itemId))
            self.precioTotal += float(item.price) * float(cantidad)
            lista.append((id, item, cantidad))
        return lista

    def getPrice(self):
        """ funcion parcial, antes se debe llamar a getItems. """
        return self.precioTotal

    def get(self, id):
        """ retorna el pedido con el id solicitado """
        for tuple  in self.session['pedidos']:
            if tuple[0] == id:
                return tuple
        else:
            raise ValueError("el id de pedido no es válido.")

    def borrar(self, id):
        pedido = self.get(id)
        list = self.session['pedidos']
        list.remove(pedido)
        self.session['pedidos'] = list

    def modificarCantidad(self, id):
        pedido = list(self.get(id))
        lista = self.session['pedidos']
        position=lista.index(pedido)
        pedido[2] = int(self.request.POST['cantidad'])
        lista[position]=tuple(pedido)
        self.session['pedidos'] = lista
