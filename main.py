class Asiento:
    def __init__(self,color,precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,col):
        if(col=="rojo" or col=="verde" or col=="Amarillo" or col=="negro" or col=="blanco"):
            self.color=col
class Motor:
    def __init__(self,numeroCilindro,tipo,registro):
        self.numeroCilindro=numeroCilindro
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,r):
        self.registro=r
    def asignarTipo(self,t):
        if(t=="electrico" or t=="gasolina"):
            self.tipo=t
    
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        
    def cantidadAsientos(self):
        contta=0
        for a in self.asientos:
            if (isinstance(a,Asiento)):
                contta+=1
        return contta
    def verificarIntegridad(self):
        for a in self.asientos:
            if isinstance(a,Asiento)== True and(self.registro != a.registro or a.registro != self.motor.registro):
                return"Las piezas no son originales"
        return"Auto original"

