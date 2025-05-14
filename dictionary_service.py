from abc import ABC, abstractmethod
from tkinter import *
class dictionary_service(ABC):
    @abstractmethod
    def read():
        pass
    @abstractmethod
    def delete():
        pass
    @abstractmethod
    def post():
        pass
    @abstractmethod
    def update():
        pass
class mock_service(dictionary_service):
    def __init__(self, path):
        self.path = path
    def read(self, word):
        raise Exception("asbndijashbdib") 
        found = False
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                for line in f:
                    i = 0
                    en = ""
                    while i < len(line):
                        if line[i] == ":":
                            break
                        en = en + line[i]
                        i = i + 1
                    if en == word:
                        translation = line[i + 2:]
                        found = True
                        break
            if not found:
                return print("Word not found.")
        except Exception as e:
            return e
        return print(translation)
    def delete(self, word):
        deleted = False
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(self.path, "w", encoding="utf-8") as f:
                for line in lines:
                    i = 0
                    en = ""
                    while i < len(line):
                        if line[i] == ":":
                            break
                        en = en + line[i]
                        i = i + 1
                    if word != en:
                        f.write(line)
                    else:
                        deleted = True
            if deleted:
                return print(word + " is deleted.")
            else:
                return print(word + " is not in the dictionary.")
        except Exception as e:
            return e
    def post(self, en, th):
        if en and th:
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(f"{en}: {th}\n")
            return print(en + " and " + th + " has been added.")
    def update(self, en, th):
        updated = False
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(self.path, "w", encoding="utf-8") as f:
                for line in lines:
                    i = 0
                    word = ""
                    while i < len(line):
                        if line[i] == ":":
                            break
                        word = word + line[i]
                        i = i + 1
                    if word == en:
                        translation = line[i + 2:-1] + ", " + th
                        if th not in translation:
                            translation.append(th)
                        f.write(f"{en}: {translation}\n")
                        updated = True
                    else:
                        f.write(line)
            if not updated:
                return print("Word not found.")
            else:
                return print("Translation added.")
        except Exception as e:
            return e