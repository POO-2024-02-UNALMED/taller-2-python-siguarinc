class Asiento:
    def __init__(self,color,precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
        def cambiarColor(self,col):
            if(col=="rojo"):
                self.color=col
                return
            elif(col=="verde"):
                self.color=col
                return
            elif(col=="Amarillo"):
                self.color=col
                return
            elif(col=="negro"):
                self.color=col
                return
            elif(col=="blanco"):
                self.color=col
                return
            else:
                return

class Motor:
    def __init__(self,numeroCilindro,tipo,registro):
        self.numeroCilindro=numeroCilindro
        self.tipo=tipo
        self.regristro=registro
        def cambiarRegistro(self,r):
            self.registro=r
            return
        def asignarTipo(self,t):
            if(t=="electrico"):
                self.tipo=t
                return
            elif(t=="gasolina"):
                self.tipo=t
                return
            else:
                return
    
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
            for a in asientos:
                if (isinstance(a,Asiento)):
                    contta+=1
            return contta
        def verificarIntegridad(self):
            for a in self.registro:
                if isinstance(a,Asiento)== True and((a.registro!=self.registro)or(self.registro!=registro)):
                    return"Las piezas no son originales"
            return"Auto original"

