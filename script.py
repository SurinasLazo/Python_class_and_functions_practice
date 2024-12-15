# Nev: Surinas Lazo Marcell



class Palack:
    def __init__(self,ital,max_urtartalom,jelenlegi_urtartalom = 1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = jelenlegi_urtartalom


    def _jelenlegi_urtartalom(self):
            return self._jelenlegi_urtartalom


    def _jelenlegi_urtartalom(self,mennyiseg):
        if mennyiseg>self.max_urtartalom:
             self._jelenlegi_urtartalom = self.max_urtartalom
        elif mennyiseg == 0:
            self._jelenlegi_urtartalom = 0
            self.ital=None
        else:
            self._jelenlegi_urtartalom = mennyiseg

    def suly(self):
        return (self.max_urtartalom/35+self._jelenlegi_urtartalom)

    def __str__(self):
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

    def __eq__(self, other):
        if isinstance(other,Palack):
            return (self.ital == other.ital and self.max_urtartalom== other.max_urtartalom and self._jelenlegi_urtartalom==other._jelenlegi_urtartalom)
        else:
            return False

    def __iadd__(self, other):

        if isinstance(other,Palack):
            if self.ital is None:
                self.ital = other.ital
                self._jelenlegi_urtartalom = other._jelenlegi_urtartalom
            if self.ital == other.ital:
                osszeg = self._jelenlegi_urtartalom + other._jelenlegi_urtartalom

                if osszeg > self.max_urtartalom:
                    self._jelenlegi_urtartalom = self.max_urtartalom
                else:
                    self._jelenlegi_urtartalom = osszeg
            else:
                if self._jelenlegi_urtartalom > 0:
                    osszeg = self._jelenlegi_urtartalom + other._jelenlegi_urtartalom

                    if osszeg > self.max_urtartalom:
                        self._jelenlegi_urtartalom = self.max_urtartalom
                    else:
                        self._jelenlegi_urtartalom = osszeg

                    self.ital = "keverek"
                else:
                    self.ital = other.ital
                    self._jelenlegi_urtartalom = other._jelenlegi_urtartalom

            return self

class VisszavalthatoPalack(Palack):
    def __init__(self,ital,max_urtartalom,_jelenlegi_urtartalom=1,palackdij=25):
        super().__init__(ital,max_urtartalom,_jelenlegi_urtartalom)
        self.palackdij = palackdij

    def __str__(self):
        return f"VisszavalthatoPalack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

class Rekesz:
    def __init__(self,max_teherbiras):
        self.max_teherbiras = max_teherbiras
        self.palackok= []

    def suly(self):
        ossztomeg=0
        for palack in self.palackok:
            ossztomeg+=palack.suly()
        return ossztomeg

    def uj_palack(self,palack):
        if self.max_teherbiras >= self.suly()+palack.suly():
            self.palackok.append(palack)

    def osszes_penz(self):
        osszeg=0
        for palack in self.palackok:
            if isinstance(palack,VisszavalthatoPalack):
                osszeg+=palack.palackdij
        return osszeg