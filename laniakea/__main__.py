import threading

class MainLoop(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def main_iteration():
    print("Hello World!")

main_loop = MainLoop(5, main_iteration)
main_loop.start();
