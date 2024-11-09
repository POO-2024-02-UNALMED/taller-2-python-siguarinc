class Asiento:
    color=""
    precio=0
    registro=0
    def cambiarColor(self,col):
        if(col=="rojo"):
            color=col
            return
        elif(col=="verde"):
            color=col
            return
        elif(col=="Amarillo"):
            color=col
            return
        elif(col=="negro"):
            color=col
            return
        elif(col=="blanco"):
            color=col
            return
        else:
            return

class Motor:
    numeroCilindro=0
    tipo=""
    registro=0
    def cambiarRegistro(self):
        return
    def asignarTipo(self,t):
        if(t=="electrico"):
            tipo=t
            return
        elif(t=="gasolina"):
            tipo=t
            return
        return
    
class Auto():
    cantidadCreados=""
    def __init__():
        modelo=""
        precio=0
        marca=""
        registro=0
        Asiento.registro=[]
        self.Motor=motor
    def cantidadAsientos():
        contta=0
        for a in Asiento.registro:
            if (isinstance(a,Asiento)):
                contta+=1
                return
    def verificarIntegridad():
        for a in Asiento.registro:
            if (isinstance(a,Asiento)!=Motor.registro!=Auto.registro):
                return"Las piezas no son originales"
            else:
                return"Auto original"

