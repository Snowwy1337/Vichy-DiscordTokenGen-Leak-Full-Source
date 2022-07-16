from colorama import Fore, init; init()
import time, threading, toml

__lock__, __config__ = threading.RLock(), toml.loads(open('../config/config.toml', 'r+').read())

class Benchmak:
    def __init__(self, bench_name: str):
        self.start_time = time.time()
        self.bench_name = bench_name
    
    def end(self):
        if __config__['perf']['benchmark_mode']:
            with __lock__:
                elapsed = time.time() - self.start_time
                color = Fore.LIGHTWHITE_EX

                if elapsed <= 0.5:
                    color = Fore.LIGHTGREEN_EX
                elif elapsed < 1:
                    color = Fore.GREEN

                if elapsed >= 1:
                    color = Fore.YELLOW
                
                if elapsed > 2:
                    color = Fore.RED
                
                if elapsed > 5:
                    color = Fore.LIGHTRED_EX

                print(f'{color}[BENCHMARK] [{self.bench_name.upper()}] This task as take {elapsed}s{Fore.RESET}')

                if __config__['logs']['save_benchmark']:
                    with open(f'../data/logs/benchmark.log', 'a+') as f:
                        f.write(f'[{self.bench_name.upper()}] [{elapsed}s]\n')