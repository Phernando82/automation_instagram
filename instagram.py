import pyautogui
import webbrowser
from time import sleep
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

while True:
    # 1 - Navegar até o Instagram
    webbrowser.open('https://www.instagram.com/')
    # login = pyautogui.locateCenterOnScreen('instagram.png')
    # pyautogui.click(login[0], login[1], duration=0.5)
    sleep(2)
    # 2 - Entrar com o usuário
    pyautogui.press(['tab', 'tab'])     
    escrever_frase('nandovalverde@gmail.com')
    sleep(1)
    # 3 - Entrar com a senha
    pyautogui.press('tab')
    escrever_frase('XXXXXXXXXXX')
    sleep(2)
    # 4 - Clicar em "log in"
    pyautogui.press(['tab', 'tab'])
    pyautogui.press('space')
    sleep(4)
    # 5 - Clicar em "Not now" para não salvar navegador
    # 6 - fechar janela de "salvar senha"
    # pyautogui.press(['tab', 'tab', 'space']) 
    # 7 - Pesquisar pela página
    pyautogui.click(876,121, duration=2)
    sleep(5)
    # 8 - Entrar na página
    pyautogui.typewrite('pearljam')
    sleep(2)
    pyautogui.click(879,221, duration=2)
    sleep(3)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(544,969, duration=2)
    sleep(3)
    # 10 - Verificar se já curti ou não aquela postagem
    curtido = pyautogui.locateCenterOnScreen('curtido.png')
    sleep(1)
    # 11 - Se já tiver curtido não fazer nada e pausar o bot por 24 horas 
    if curtido is not None:
        sleep(86400) # 24 horas
    # 12 - Se não tiver curtido, curtir a foto
    elif curtido == None:
        pyautogui.click(1118,833, duration=2)
        sleep(2)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(1167,831, duration=2) #clica no icone comentario
        sleep(2)
        pyautogui.click(1183,966, duration=2) # clica no campo comentario
        pyautogui.typewrite('Very Cool!')
        sleep(1)
        pyautogui.click(1670,970, duration=2) # clica em post
        # 14 - pausar por 24 horas e então rodar tudo de novo
        sleep(86400)