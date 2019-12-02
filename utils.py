import os

def load(self, src, ext):
    src = os.path.join(src)
    files = []
    for file in os.listdir(src):
        if file.lower().endswith(ext.lower()):
            files.append(os.path.join(src, file))
    return files