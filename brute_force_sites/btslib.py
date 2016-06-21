__author__ = 'Leonardo'
import winsound
import requests
import webbrowser
import time


class Site:

    url = ''

    def __init__(self, url):
        self.url = url

    def brute_force(self, go_hardcore=False, do_beep=False, open_done=False):
        done = False
        if go_hardcore:
            t = 0
        else:
            t = 1

        while not done:
            try:
                r = requests.get(self.url)
                done = True

            except Exception as e:
                print("[*] ERROR \t Trying Again")

            time.sleep(t)
        print("[*] DONE \t " + self.url)
        if do_beep:
            for s in range(10):
                winsound.Beep(300, 2000)
                time.sleep(2)
        if open_done:
            webbrowser.open(self.url)

    def get_error_string(self):
        try:
            error = requests.get(self.url)
        except Exception as e:
            error = str(e)
        if str(error) == "<Response [200]>":
            error = False
        return error

if __name__ == '__main__':
    test = Site("http://google.com.br")
    test.brute_force(open_done=True)