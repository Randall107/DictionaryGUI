from tkinter import *
from base_vm import baseVM
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class DeleteTab(Frame, baseVM):
    def __init__(self, parent, dictionary_service):
        Frame.__init__(self, parent)
        baseVM.__init__(self, self)
        self.dictionary_service = dictionary_service
        Label(self, text="Delete:").pack()

        self.en_entry = Entry(self)
        self.en_entry.pack()
        self.en_entry.bind("<KeyRelease>", self.validate)

        self.button = Button(self, text="Delete", command=self.submit)
        self.button.pack()
        self.button["state"] = "disabled"
    def validate(self, event=None):
        en = self.en_entry.get().lower()
        if en == "":
            self.button["state"] = "disabled"
        else:
            self.button["state"] = "normal"
    def submit(self):
        try:
            self.dictionary_service.delete(self.en_entry.get())
        except Exception as e:
            logging.error("Error calling delete", exc_info=True)