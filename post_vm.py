from tkinter import *
from base_vm import *
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class PostTab(Frame, baseVM):
    def __init__(self, parent, dictionary_service):
        Frame.__init__(self, parent)
        baseVM.__init__(self, self)
        self.dictionary_service = dictionary_service

        Label(self, text="English:").pack()
        self.en_entry = Entry(self)
        self.en_entry.pack()
        self.en_entry.bind("<KeyRelease>", self.validate)

        Label(self, text="Thai:").pack()
        self.th_entry = Entry(self)
        self.th_entry.pack()
        self.th_entry.bind("<KeyRelease>", self.validate)

        self.button = Button(self, text="Submit", command=self.submit)
        self.button.pack()
        self.button["state"] = "disabled"
    def validate(self, event=None):
        en = self.en_entry.get().lower()
        th = self.th_entry.get().lower()
        if en == "" or th == "":
            self.button["state"] = "disabled"
        else:
            self.button["state"] = "normal"
    def submit(self):
        try:
            self.dictionary_service.post(self.en_entry.get(), self.th_entry.get())
        except Exception as e:
            logging.error("Error calling post", exc_info=True)