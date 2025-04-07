class node: # 7 pierwszych warosci odpowiada tym z 1 prezentacji
    def __init__(self,t,n,pr = None , es= None , ef= None, ls= None, r= None, lf= None, ne= None):
        self.early_start = es
        self.duration = t
        self.early_finish = ef
        self.name = n
        self.late_start = ls
        self.reserve = r
        self.late_finish = lf
        self.previous = pr if pr is not None else []
        self.next = ne if ne is not None else [] 

# idk czy potrzebne sa gettery i settery ale sa jako opis na jire

    def get_es(self):
        return self.early_start
    
    def set_es(self, val):
        self.early_start = val
        
    def get_t(self):
        return self.duration
    
    def set_t(self, val):
        self.duration = val
        
    def get_ef(self):
        return self.early_finish
    
    def set_ef(self, val):
        self.early_finish = val

    def get_n(self):
        return self.name
    
    def set_n(self, val):
        self.name = val
        
    def get_ls(self):
        return self.late_start
    
    def set_ls(self, val):
        self.late_start = val
        
    def get_r(self):
        return self.reserve
    
    def set_r(self, val):
        self.reserve = val
        
    def get_lf(self):
        return self.late_finish
    
    def set_lf(self, val):
        self.late_finish = val
        
    def get_pr(self):
        return self.previous
    
    def set_pr(self, val):
        self.previous = val
        
    def get_ne(self):
        return self.next
    
    def set_ne(self, val):
        self.next = val

    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "early_start": self.early_start,
            "early_finish": self.early_finish,
            "late_start": self.late_start,
            "late_finish": self.late_finish,
            "reserve": self.reserve,
            "previous": self.previous,
            "next": self.next
        }

