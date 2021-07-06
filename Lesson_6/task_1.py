from time import sleep


class Traffic:

    def running(self):
        while True:
            print('Red STOP!')
            sleep(7)
            print('Yellow')
            sleep(2)
            print('Green GO GO!')
            sleep(7)
            print('Yellow')
            sleep(2)


traffic = Traffic()
traffic.running()