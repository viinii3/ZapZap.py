#importando o flet
import flet as ft

# Criar a função principal do aplicativo
def main(pagina):
    #Criar todas as funcionalidade
    #criar os elementos
    titulo = ft.Text('ZapZap')
    
    tituloJanela = ft.Text('Bem-Vindo ao zapzap')
    campo_nome_usuario = ft.TextField(label='escreva seu nome no chat')
    
    chat = ft.Column()
    campo_mensagem = ft.TextField(label='digite sua mensagem')
    
    def enviarMensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f'{nome_usuario}: {texto_mensagem}'
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()
    
    buttonEnviarMensagem = ft.ElevatedButton('enviar', on_click=enviarMensagem)
    
    def entrarChat(evento):
        pagina.remove(titulo)
        pagina.remove(button_iniciar)
        janela.open = False
        
        pagina.add(chat)
        pagina.add(campo_mensagem)
        pagina.add(buttonEnviarMensagem)
        pagina.update()
    
    botaoEntrar = ft.ElevatedButton('entrar no chat', on_click=entrarChat)
    janela = ft.AlertDialog(
        title=tituloJanela,
        content=campo_nome_usuario,
        actions=[botaoEntrar]
    ) 
    
    def iniciarChat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    button_iniciar = ft.ElevatedButton('Iniciar chat', on_click=iniciarChat)
    
    #adicionar os elementos
    pagina.add(titulo)
    pagina.add(button_iniciar)
    
    #criando tunel de comunicação
    def enviarMensagem_tunel(mensagem):
        textoDoChat = ft.Text(mensagem)
        chat.controls.append(textoDoChat)
        pagina.update()

    pagina.pubsub.subscribe(enviarMensagem_tunel)
    
#rodar o seu app
ft.app(main, view=ft.WEB_BROWSER)