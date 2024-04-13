class Uzel:
    """uzel spojového seznamu"""

    def __init__(self, x=None):
        self.info = x  # uložená hodnota
        self.dalsi = None  # následník


def vytvor():
    n = int(input())
    if n == 0:
        return None
    s = input().split()
    p = Uzel(int(s[0]))
    k = p
    for i in range(1, n):
        t = Uzel(int(s[i]))
        k.dalsi = t
        k = t
    return p


def vypis(p):
    if p == None:
        print('PRAZDNY')
        return
    s = p
    while s != None:
        print(s.info, end=" ")
        s = s.dalsi
    print()


def zrus_max(p):
    if p == None:
        return p

    s = p
    temp = s
    while s.dalsi != None:
        if(s.dalsi.info>temp.info):
            temp = s.dalsi
        s = s.dalsi

    s = p
    if s == temp:
        p = s.dalsi
    else:
        while s.dalsi != temp:
            s=s.dalsi

        s.dalsi = temp.dalsi

    return p

def obrat(p):
    if p == None:
        return p

    s = p
    p = None
    while s != None:
        temp = s.dalsi
        s.dalsi = p
        p = s
        s = temp
    return p

def zrus_vsechny(p, x):
    while p != None and p.info == x:
        p = p.dalsi

    if p == None:
        return p

    s = p
    while s.dalsi != None:
        if s.dalsi.info == x:
            s.dalsi = s.dalsi.dalsi
        else:
            s = s.dalsi
    return p

def pridej(p, x):
    if p == None:
        p = Uzel(x)
        return p

    s = p
    while s.dalsi != None:
        s = s.dalsi
    s.dalsi = Uzel(x)

    return p

def zrus_dva_posledni(p):
    if p == None or p.dalsi == None or p.dalsi.dalsi == None:
        return None

    s = p
    while s.dalsi.dalsi.dalsi != None:
        s = s.dalsi
    s.dalsi = None

    return p

def zrus_sude_pozice(p):
    if p == None or p.dalsi == None:
        return p

    if p.dalsi != None:
        p.dalsi = p.dalsi.dalsi

    s = p.dalsi
    while s != None and s.dalsi != None:
        s.dalsi = s.dalsi.dalsi
        s = s.dalsi

    return p

def pridej_kopii(p):
    if p == None:
        return p

    q = Uzel(p.info)
    s = p.dalsi
    temp = q

    while s != None:
        temp.dalsi = Uzel(s.info)
        s = s.dalsi
        temp = temp.dalsi
    temp.dalsi = p

    return q

def rozdel(p):
    if p == None or p.dalsi == None:
        return p, p
    l = Uzel()
    s = Uzel()
    kl,ks = l,s
    while p != None:
        q = p
        p = p.dalsi
        if q.info%2==0:
            ks.dalsi = q
            ks = q
        else:
            kl.dalsi = q
            kl = q
    ks.dalsi,kl.dalsi = None,None
    return l.dalsi, s.dalsi

a = vytvor()
vypis(a)
a,b = rozdel(a)
vypis(a)
vypis(b)