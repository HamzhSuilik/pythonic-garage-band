class Musician :
    def __init__ (self,name,musical_instrument,sound):
        self.name = name
        self.musical_instrument = musical_instrument
        self.sound = sound

    def ooo(self):
        return 'ooo'

    def __str__(self):
        return f"Name : {self.name} \n Musical Instrument : {self.musical_instrument} \n Sound : {self.sound}"

    def __repr__(self):
        return f"Name = {self.name}"

    def get_instrument (self):
        return self.musical_instrument


class Band:
    def __init__(self,name,members=[]):
        self.name = name
        self.members = members

    def play_solos(self):
        solo = []
        for player in self.members :
            solo.append(player.play_solo())
        return solo
        

    def __str__(self):
        str = f"Band Name : {self.name}\nMembers names : "
        for player in self.members :
            str = str + '\n' + player.name
        return str

    def __repr__(self):
        return f"Name : {self.name}"

    def to_list(self):
        return self.members


class Guitarist (Musician) :
    def __init__ (self,name):
        super().__init__(name,'Guitar','Rhythm')

    def __str__(self):
        return f"Name : {self.name} \n Musical Instrument : {self.musical_instrument} \n Sound : {self.sound}"

    def __repr__(self):
        return f"Name = {self.name}"

    def get_instrument (self):
        return self.musical_instrument

    
    def play_solo (self):
        return self.sound

class Bassist (Musician) :
    def __init__ (self,name):
        super().__init__(name,'bass','Music')
    def __str__(self):
        return f"Name : {self.name} \n Musical Instrument : {self.musical_instrument} \n Sound : {self.sound}"

    def __repr__(self):
        return f"Name = {self.name}"

    def get_instrument (self):
        return self.musical_instrument

    
    def play_solo (self):
        return self.sound

class Drummer (Musician):
    def __init__ (self,name):
        super().__init__(name,'drum','beat the drum')
    def __str__(self):
        return f"Name : {self.name}\nMusical Instrument : {self.musical_instrument}\nSound : {self.sound}"

    def __repr__(self):
        return f"Name = {self.name}"

    def get_instrument (self):
        return self.musical_instrument

    def play_solo (self):
        return self.sound


