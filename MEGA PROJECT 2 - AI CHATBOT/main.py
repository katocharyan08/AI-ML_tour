import time
import pyautogui
import pyperclip
import os
from openai import OpenAI

# client = OpenAI(
#     api_key = os.getenv("OPENAI_API_KEY")
# )

# Give yourself a few seconds to switch to the target window
time.sleep(3)

# Click at (1376, 1052)
pyautogui.click(1376, 1052)
time.sleep(0.2)
while True:
    # Drag to select the text
    pyautogui.moveTo(677, 193)
    pyautogui.dragTo(774, 1008, duration=0.5, button='left')

    time.sleep(0.2)

    # Copy selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')

    # Wait for clipboard to update
    time.sleep(0.2)

    # Store clipboard text in a variable
    copied_text = pyperclip.paste()

    #For diselect
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

    #click
    pyautogui.click(988,978)

    #paste
    pyautogui.hotkey('ctrl','v')

    #prss enter 
    pyautogui.press('enter')