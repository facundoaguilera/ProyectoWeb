from .carro import Carro
def importe_total_carro(request): #este archivo context_procssor debemos agregarlo al settings en context processors para que sea una variable global
    total=0
    
    if request.user.is_authenticated and request.session.__contains__('carro'):
        for key,value in request.session['carro'].items():
            total=total+float(value['precio'])
        return {'importe': total}
    else:
        return {'importe': 0}
    #return {'importe_total_carro': 5}