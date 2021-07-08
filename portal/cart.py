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
        #id = self.newId()
        pedido = (self.request.POST['item'], self.request.POST['cantidad'])
        list = self.session['pedidos']
        list.append(pedido)
        self.session['pedidos'] = list
