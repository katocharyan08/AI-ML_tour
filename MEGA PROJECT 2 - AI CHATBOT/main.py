import time
import pyautogui
import pyperclip
import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
def  isLastMessageFromSender(chat_log, sender_name = "Mummy Ji"):
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in  messages:
        return True
    return False

time.sleep(5)


pyautogui.click(1376, 1052)
time.sleep(0.5)
while True:
  
    pyautogui.moveTo(1838,198)
    pyautogui.dragTo(1815,1025 , duration=0.5, button='left')

    time.sleep(3)

   
    pyautogui.hotkey('ctrl', 'c')

  
    time.sleep(0.2)

    
    copied_text = pyperclip.paste()

   
    pyautogui.click(737, 288)

    print("Copied Text:")
    print(copied_text)
    time.sleep(2)
    if isLastMessageFromSender(copied_text):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """You are a prson named Aryan, eho epeaks hindi as well as english. 
                                                You are from india. you analyze copied_text and respomd like Aryan. 
                                                Output should be the next chat response as Arayn and only text message. """},
                {"role": "user", "content": copied_text},
            ]
        )

        response = completion.choices[0].message.content
        response = 'hanji, kaise ho? '
        pyperclip.copy(response)

    
        pyautogui.click(995,975)

    
        pyautogui.hotkey('ctrl','v')

        
        pyautogui.press('enter')
            