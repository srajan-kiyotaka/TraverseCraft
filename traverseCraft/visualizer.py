import platform
import ctypes
def check_os():
    system = platform.system()
    
    if system == 'Windows':
        print("Running on Windows")
        windows_visualization()
    elif system == 'Linux':
        print("Running on Linux")
        linux_visualization()
    elif system == 'Darwin':
        print("Running on macOS")
        mac_visualization()
    else:
        print(f"Unknown operating system: {system}")

def windows_visualization():
    ctypes.windll.user32.MessageBoxW(0, "Your message", "Your title", 1)
def linux_visualization():
    title = "Your title"
    message = "Your message"
    show_message_box(title, message)
    libc = ctypes.CDLL("libc.so.6")
    
    display = libc.XOpenDisplay(None)
    if not display:
        raise Exception("Failed to open display")

    root = libc.XDefaultRootWindow(display)
    window = libc.XCreateSimpleWindow(display, root, 10, 10, 300, 200, 1, 0, 0xFFFFFF)

    WM_DELETE_WINDOW = libc.XInternAtom(display, "WM_DELETE_WINDOW", 0)
    libc.XSetWMProtocols(display, window, ctypes.byref(WM_DELETE_WINDOW), 1)
    libc.XSetStandardProperties(display, window, title, title, 0, None, 0, None)

    libc.XMapWindow(display, window)
    libc.XFlush(display)
    
    text = ctypes.c_char_p(message.encode('utf-8'))
    title = ctypes.c_char_p(title.encode('utf-8'))
    libc.XStoreName(display, window, title)
    libc.XSetIconName(display, window, title)

    WM_DELETE_WINDOW_MASK = (1 << 16)
    XEvent = ctypes.c_ulong * 32
    event = XEvent()

    while True:
        libc.XNextEvent(display, ctypes.byref(event))
        if event.type == WM_DELETE_WINDOW_MASK:
            break
def mac_visualization():
    pass


if __name__ == "__main__":
    check_os()
