class Asiento:
    def __init__(self,color,precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
        def cambiarColor(self,cambiarColor):
            self.cambiarColor=cambiarColor
            if(cambiarColor=="rojo"):
                color=cambiarColor
                return
            elif(cambiarColor=="verde"):
                color=cambiarColor
                return
            elif(cambiarColor=="Amarillo"):
                color=cambiarColor
                return
            elif(cambiarColor=="negro"):
                color=cambiarColor
                return
            elif(cambiarColor=="blanco"):
                color=cambiarColor
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
            self.tipo=t
            if(t=="electrico"):
                tipo=t
                return
            elif(t=="gasolina"):
                tipo=t
                return
            else:
                return
    
class Auto():
    cantidadCreados=""
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        
        def cantidadAsientos(self):
            contta=0
            for a in Asiento.registro:
                if (isinstance(a,Asiento)):
                    contta+=1
            return contta
        def verificarIntegridad():
            for a in Asiento.registro:
                if isinstance(a,Asiento)== True and((a.registro!=self.registro)or(self.registro!=registro)):
                    return"Las piezas no son originales"
                else:
                    return"Auto original"

