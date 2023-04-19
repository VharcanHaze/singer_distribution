# http://bspaans.github.io/python-mingus/index.html

from mingus.containers import Note
from mingus.core.keys import *

class Singer():
    def __init__(self, name: str, low: Note, high: Note):
        self.name = name
        self.low = low
        self.high = high
        self.range = int(high)-int(low)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.low} til {self.high}, {self.range} halvtoner"

class Role():
    def __init__(self, name: str, low: Note, high: Note, singer: Singer = None):
        self.name = name
        self.low = low
        self.high = high
        self.range = int(high)-int(low)
        self.singer = singer
    
    def check_singer(self, singer: Singer):
        return singer.low <= self.low and self.high <= singer.high
    
    def assign_singer(self, singer: Singer):
        if self.check_singer(singer) == True:
            self.singer = singer
        else:
            pass

class Song():
    def __init__(self,
                 name_revy: str, name_org:str,
                 key_org: Key, keys_band: list[Key],
                 roles: list[Role]):
        self.name_revy = name_revy
        self.name_org = name_org
        self.key_revy = key_org
        self.key_org = key_org
        self.keys_band = keys_band
        self.keys_possible = keys_band
        self.roles = roles

    def get_band_keys(self):
        return [k.name for k in self.keys_band]
    
    def get_possible_keys(self):
        return [k.name for k in self.keys_possible]
    
    def transpose_new_key(self, new_key: Key):
        self.key_revy = Key(new_key)


# Testing
jeppe = Singer("Jeppe", Note("G",2), Note("G",4))

tadaSanger0 = Role("Rus", Note("C",3), Note("C",4))
tadaSanger1 = Role("TA", Note("D",2), Note("D",4))

tada = Song("RevySang", "OriginalSang",
            Key("C#"), [Key("C"), Key("F")],
            [tadaSanger0, tadaSanger1])

tadaSanger0.assign_singer(jeppe)

print(tadaSanger0.singer)