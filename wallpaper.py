import ctypes


# Here we will have setting wallpaper for all OS's I only know Windows for now

def win(path):
    # This code is based on the following two links
    # http://mail.python.org/pipermail/python-win32/2005-January/002893.html
    # http://code.activestate.com/recipes/435877-change-the-wallpaper-under-windows/
    cs = ctypes.c_wchar_p(path)
    return ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, cs, 0)
