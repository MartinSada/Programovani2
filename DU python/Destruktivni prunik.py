class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

#################################################

def IntersectionDestruct(a,b):
    """ destruktivni prunik dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """
    if a == None or b == None:
        return None
    else:
        head = tail = None

        while a != None and b != None:
            if a.x == b.x:
                if head == None:
                    head = tail = a
                else:
                    tail.dalsi = a
                    tail = a

                while a.dalsi != None and a.x == a.dalsi.x:
                    a = a.dalsi
                while b.dalsi != None and b.x == b.dalsi.x:
                    b = b.dalsi

                a = a.dalsi
                b = b.dalsi

                tail.dalsi = None

            elif a.x < b.x:
                a = a.dalsi
            else:
                b = b.dalsi
        return head

#################################################

VytiskniLSS( IntersectionDestruct( NactiLSS(), NactiLSS() ) )