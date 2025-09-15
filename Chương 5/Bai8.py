import os


def get_filename(path: str):
    return os.path.basename(path)


def get_filename_no_ext(path: str):
    return os.path.splitext(os.path.basename(path))[0]


# path = r"d:\music\muabui.mp3"
path = input("Nhập đường dẫn: ")
print(get_filename(path))
print(get_filename_no_ext(path))
