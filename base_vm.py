from abc import ABC, abstractmethod
from dictionary_service import *
from tkinter import *
class baseVM(ABC):
    @abstractmethod
    def __init__(self, service):
        pass
    @abstractmethod
    def validate():
        pass
    @abstractmethod
    def submit():
        pass