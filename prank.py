import time
time.sleep(0.8)
print('Mecrosoft Wendows [Version 10.0.19045.5247](c) Корпорация Микрософт (Mecrosoft Corporation). Все права защищены.')
choose = input('Do you want to formate disk C:? (y/n) ')
if choose == 'y':
    import time
    import sys
    loading_symbols = ['|', '\\', '/', '-']
    def loading_animation(duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            for symbol in loading_symbols:
                sys.stdout.write('\r' + symbol)
                sys.stdout.flush() 
                time.sleep(0.2)  
    loading_animation(8)
    print('Prank!')
    time.sleep(1.6)
    while True:
        print('HAHAHA')
if choose == 'n':
    pass
if choose == 'i':
    whoareme = input('Youuu? ')
    if whoareme == 'dweb':
        print('I known it.')
    if whoareme == 'Mecrosoft':
        print('You are Mecrosoft? Uh.. What?')
    if whoareme == 'Sigma':
        print('https://yandex.ru/images/search?pos=4&from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FrT83T2Trf6I%2Fmaxresdefault.jpg&text=sigma+face&rpt=simage&lr=239')
input('Press Enter to exit...')