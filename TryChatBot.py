from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear un objeto de chatbot
chatbot = ChatBot(
    'MiChatbot', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ],
    database_uri='sqlite:///database.db'
)

# Entrenador
trainer = ChatterBotCorpusTrainer(chatbot)

# Entrenar al chatbot con los datos en español
trainer.train('chatterbot.corpus.spanish')

# Función para interactuar con el chatbot
def hablar_con_chatbot():
    print("¡Hola! Soy tu chatbot. Escribe 'salir' para terminar la conversación.")
    
    while True:
        try:
            entrada_usuario = input("Tú: ")
            
            if entrada_usuario.lower() == 'salir':
                print("Chatbot: ¡Hasta luego!")
                break
            
            respuesta = chatbot.get_response(entrada_usuario)
            print(f"Chatbot: {respuesta}")
        
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Ejecutar la función de conversación
hablar_con_chatbot()
