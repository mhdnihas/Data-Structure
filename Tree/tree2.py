class FileSystemNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

# Creating a sample folder structure tree
root = FileSystemNode("Root")
root.children.append(FileSystemNode("Documents"))
root.children.append(FileSystemNode("Pictures", is_file=True))
root.children[0].children.append(FileSystemNode("Work"))
root.children[0].children.append(FileSystemNode("Personal"))