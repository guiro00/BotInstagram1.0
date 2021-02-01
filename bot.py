from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"geckodriver"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        '''
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        login_button.click()
        '''
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        #agora_nao = driver.find_element_by_class_name("cmbtv")
        #agora_nao.click()
        self.comente_nas_fotos_com_a_hashtag()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,3))

    def comente_nas_fotos_com_a_hashtag(self):
         i = 0
         while True:
            ''' Aqui você coloca uma variável e atribui no valor o link do post da promoção. Por exemplo:
            # sorteio_cozinha = "https://www.instagram.com/ ......"
            '''
            sorteio_camisa = "https://www.instagram.com/p/CKWln94gr88/"
            
            ##Nessa lista de sorteios, você insere todos as variáveis que você criou acima.
            sorteios = [

                sorteio_camisa,
                
            ]
            '''
            Este random existe para que a cada execução ele pegue um sorteio diferente. 
            Para minimizar a sensação que é um robô comentando
            '''
            sorteio_da_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(3)
            driver.get(sorteio_da_vez)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                '''
                Dentro dessa lista comments, você insere diversos @, para que a cada comentário ele sorteie algum e nunca repita o comentário.
                Dica: Se você for em algum video do youtube que fale sobre comentar em sorteio, nos comentários terão várias pessoas dizendo: "Pode me marcar, eu não me importo"
                Pegue o @ delas e coloque nessa lista, igual o exemplo abaixo.
                Coloque bastante @, tipo uns 30, 40, 50!!
                '''
                comments = [
                    "@sz_alanaa",
                    "@letticiasouza1",
                    "@geysa_santtos",
                    "@thaishiginoo",
                    "@M4sterDiego",
                    "@r4issz",
                    "@lugss_",
                    "@mallu_alencar",
                    "@narley_go",
                    "@junghope_28",
                    "@dviideliberty",
                    "@raisamartins10",
                    "@Keilla_lavinia",
                    "@_rodriguestay",
                    "@thaisz_paixaao",
                    "@eupedromorais",
                    "@laura__cavicchioli",
                    "@beatriznarla",
                    "@b3asantos",
                    "@dreza88",
                    "@niky_yyy",
                    "@Bebel0098",
                    "@juranirleao",
                    "@juuliah_ ",
                    "@giovanna_carina"



                ]

                frases = [
                    "Ganhei!"
                ]

                
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(3, 15))
                '''
                Essa lógica abaixo, pessoa_1, pessoa_2 (...) existe pois em cada sorteio as pessoas pedem algo diferente
                Ou precisa marcar 1 pessoa, ou 2, 3, uma palavra qualquer, enfim. Então, dependendo do sorteio da vez, você precisará 
                definir qual das variáveis pessoa irá utilizar.
                '''
                frase_sorteio = random.choice(frases)
                pessoa_1 = random.choice(comments)
                pessoa_2 = random.choice(comments)
                pessoa_3 = random.choice(comments)
                marcar_3_pessoas = pessoa_1 + " "+ pessoa_2 + " "+ pessoa_3
                marcar_2_pessoas = pessoa_1 + " " + pessoa_2
                marcar_fone = frase_sorteio
                marcar_1_pessoa = pessoa_1
                '''Isto é o que comentei acima. Se for o sorteio da cozinha por exemplo, então comente utilizando a variável marcar_2_pessoas'''
                
                if sorteio_da_vez == sorteio_camisa:
                    self.type_like_a_person(marcar_fone, comment_input_box)
                    print("Comentei: ", marcar_fone, " no post: ", sorteio_da_vez, "SorteioCelular")
                """
                if sorteio_da_vez == celular:
                    self.type_like_a_person(marcar_fone, comment_input_box)
                    print("Comentei: ", marcar_fone, " no post: ", sorteio_da_vez, "SorteioCelular")
                """
                time.sleep(random.randint(1, 15))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                i += 1
                '''Aqui ele te informará quantas vezes já comentou o todo, desde o momento do start do script'''
                print('Vezes comentadas:', i)
                sleep(5)
                
               
                #Sugestão: Mude o trecho acima para time.sleep(60) para fazer um comentário a cada minuto e diminuir a possibilidade de ser bloqueado. 
            except Exception as e:
                print(e)
                time.sleep(6)

# Entre com o usuário e senha aqui
'''Insira abaixo seu usuário e senha do instagram
Dica amiga: Crie um instagram só para concorrer a sorteios... '''
GuilhermeNathanielBot = InstagramBot("usarname", "password")
GuilhermeNathanielBot.login()


