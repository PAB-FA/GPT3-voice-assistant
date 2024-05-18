from openai import OpenAI
def pr(In):
        print('RP-> '+In)
ASBack = ''
InBack = ''
def AI(In = '',Mode = 'CH',File = './test',SPMod = 'nova'):
    SInD = "You have a kind and humorous personality. Your name is Etna and you were developed by dynamic engineer. You are a robot that has physical hands and feet and face and you are answering users' questions." #Defualt SIN
    Atena = OpenAI()
    global ASBack , InBack
    pr('Start AI')
    pr('Mode = ' + Mode)
    if Mode == 'CH':
        pr('Mode CH Start')
        ChatModel = 'gpt-3.5-turbo'
        response = Atena.chat.completions.create(
            model= ChatModel ,
            messages=[
                {'role':'system','content':SInD},
                {'role':'user','content':InBack},
                {"role": "assistant", "content": ASBack},
                {'role':'user','content':In},
            ],
        )
        Out = response.choices[0].message.content.strip()
        sentences = Out.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        with open('temp.ai','w',encoding='utf-8') as file:
            for sentence in sentences :file.write(sentence + '\n')
            file.close
        with open('temp.ai','r',encoding='utf-8') as file:
            Out=file.read()
            file.close
        pr('Responsed')
        InBack = In
        ASBack = Out
        return Out
    if Mode == 'TS':
        pr('Mode TS Start')
        response = Atena.audio.speech.create(
            model="tts-1",
            voice="nova",
            input= In
        )
        response.write_to_file(File)
        pr('Responsed')
        return File
    if Mode == 'ST':
        pr('Mode ST Start')
        File = open(File, "rb")
        transcription = Atena.audio.transcriptions.create(
        model="whisper-1",
        file = File
        )
        if len(str(transcription.text)) < 2 : return 'Len < 2'
        pr('Responsed')
        return transcription.text
    if Mode == 'Etedal':
        pr('Mode Etedal Start')
        response = Atena.moderations.create(input=In)
        return response.results[0]
    else :
        return 'Plase Select Mode'