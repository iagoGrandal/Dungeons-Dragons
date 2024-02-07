from math import ceil


class characteristics():
    def __init__(self, stre, dexe, cons, inte, wisd, char):
        self._stre = stre
        self._dexe = dexe
        self._cons = cons
        self._inte = inte
        self._wisd = wisd
        self._char = char

    #getters
    def get_stre(self):
        return self._stre
    def get_dexe(self):
        return self._dexe
    def get_cons(self):
        return self._cons
    def get_inte(self):
        return self._inte
    def get_wisd(self):
        return self._wisd
    def get_char(self):
        return self._char
    
    #setters
    def set_stre(self, stre):
        self._stre = stre
    def set_dexe(self, dexe):
        self._dexe = dexe
    def set_cons(self, cons):
        self._cons = cons
    def set_inte(self, inte):
        self._inte = inte
    def set_wisd(self, wisd):
        self._wisd = wisd
    def set_char(self, char):
        self._char = char
    
    def salvations(self):
        pass


class salvations(characteristics):
    def __init__(self, stre, dexe, cons, inte, wisd, char):
        super().__init__(ceil((stre-10)/2),ceil((dexe-10)/2),
                         ceil((cons-10)/2),ceil((inte-10)/2),
                         ceil((wisd-10)/2),ceil((char-10)/2))
    
    

def format(list):
    for i in range(list):
        print(f"{i}\t", end = "", i = i)

def characteristics_creator():
    stre = 8
    dexe = 8
    cons = 8
    inte = 8
    wisd = 8
    char = 8
    counter = 0
    charac = [stre, dexe, cons, inte, wisd, char]
    charact = ["strength (1)", "dexerity (2)", "constitution (3)", "inteligence (4)", "wisdom (5)", "charism (6)"]

    while counter <= 27:
        print(f"please select a charateristic to increase!\n")
        format(charact)
        format(charac)
        chosen = int(input())

        for i in range(1, charac):
            if chosen == i and charac[chosen - 1] <= 16:
                if charac[chosen-1] <= 13:
                    counter += 1
                else:
                    counter += 2
                if counter <= 27:
                    charac[chosen-1] += 1

    return characteristics(stre, dexe, cons, inte, wisd, char)