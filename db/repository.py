import abc
from model.chordmaker import *


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_chord(self) -> list[Chord]:
        raise NotImplementedError

