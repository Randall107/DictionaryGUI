from tkinter import *
from tkinter import ttk
from dictionary_service import *

from post_vm import PostTab
from delete_vm import DeleteTab
from update_vm import UpdateTab
from read_vm import ReadTab

class VocabApp:
    def __init__(self, root):
        root.title("Vocab Manager")

        notebook = ttk.Notebook(root)
        m = mock_service(r"/run/media/harddisk/Documents/Dictionary/dummy.txt")
        r = ReadTab(notebook, m)
        #d = DeleteTab(notebook, m)  
        #u = UpdateTab(notebook, m)
        #p = PostTab(notebook, m)
        notebook.add(r, text="Read")
        #notebook.add(d, text="Delete")
        #notebook.add(u, text="Update")
        #notebook.add(p, text="Post")

        notebook.pack(expand=True, fill="both")


if __name__ == "__main__":
    root = Tk()
    app = VocabApp(root)
    root.mainloop()