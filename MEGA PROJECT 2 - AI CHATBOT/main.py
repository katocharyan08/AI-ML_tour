import time
import pyautogui
import pyperclip
import os
from openai import OpenAI

# client = OpenAI(
#     api_key = os.getenv("OPENAI_API_KEY")
# )


time.sleep(5)


pyautogui.click(1376, 1052)
time.sleep(0.2)
while True:
  
    pyautogui.moveTo(677, 193)
    pyautogui.dragTo(774, 1008, duration=0.5, button='left')

    time.sleep(0.2)

   
    pyautogui.hotkey('ctrl', 'c')

  
    time.sleep(0.2)

    
    copied_text = pyperclip.paste()

   
    pyautogui.click(737, 288)

    print("Copied Text:")
    print(copied_text)

    # completion = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": """You are a prson named Aryan, eho epeaks hindi as well as english. 
    #                                         You are from india. you analyze copied_text and respomd like Aryan. 
    #                                         Output should be the next chat response as Arayn. """},
    #         {"role": "user", "content": copied_text},
    #     ]
    # )

    # response = completion.choices[0].message.content
    response = 'hanji'
    pyperclip.copy(response)

   
    pyautogui.click(988,978)

  
    pyautogui.hotkey('ctrl','v')

     
    pyautogui.press('enter')
    