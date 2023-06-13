class Carrito:
    def__init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, zapatilla):
        id = str(zapatilla.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": zapatilla.id_producto,
                "nombre": zapatilla.nombre,
                "talla": zapatilla.talla,
                "acumulado": zapatilla.precio
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["acumulado"] += zapatilla.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, zapatilla):
        id = str(zapatilla.id_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    def restar(self, zapatilla):
        id = str(zapatilla.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= zapatilla.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(zapatilla)
            self.guardar_carrito()
    def limpiar(self):
        self.session["carrito"] ={}
        self.session.modified = True