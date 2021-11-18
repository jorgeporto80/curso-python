import pyttsx3

que_dice = "¡Hola! Este es el curso introductorio de Paiton. Vayanse a la recalcada de su madre."
quien_dice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

engine = pyttsx3.init()
engine.setProperty('voice',quien_dice)  # seteo de vos
engine.setProperty('rate',130)          # seteo de velocidad
engine.say(que_dice)
engine.runAndWait()

