class Vrchol:
    def __init__(self, x = None, levy = None, pravy = None):
        self.info = x          # uložená hodnota
        self.levy = levy       # levý syn
        self.pravy = pravy     # pravý syn

def IsSymetric(p):
    def IsSymetricSubtree(levy, pravy):
        if levy == None and pravy == None:
            return True
        if levy == None or pravy == None:
            return False
        return IsSymetricSubtree(levy.levy, pravy.pravy) and IsSymetricSubtree(levy.pravy, pravy.levy)
    if p == None:
        return True
    return IsSymetricSubtree(p.levy, p.pravy)