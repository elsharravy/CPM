from node_class import node

def create_node(name: str, duration: int, previous: list):
    """
    Tworzy nowy obiekt node z podstawowymi danymi.
    Pozostałe wartości są inicjalizowane jako None.
    """
    return node(
        t=duration,
        n=name,
        pr=previous,
        es=None,
        ef=None,
        ls=None,
        r=None,
        lf=None,
        ne=[]
    )
