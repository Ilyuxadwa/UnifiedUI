import platform

def get_screen_resolution() -> tuple[int, int]:
    if platform.system() == "Windows":
        try:
            import ctypes, ctypes.wintypes
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.SystemParametersInfoW(48, 0, ctypes.byref(rect), 0)  # SPI_GETWORKAREA = 48
            return rect.right - rect.left, rect.bottom - rect.top
        except Exception:
            pass

    try:
        import tkinter
        root = tkinter.Tk()
        root.withdraw()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.destroy()
        return w, h
    except Exception:
        pass

    return 1920, 1080



def scale(size: str):
    return {"full": 1.0, "1/2": 0.75, "1/4": 0.5}[size]