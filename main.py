import os
import customtkinter as ctk # pip install customtkinter 
from openai import OpenAI
from dotenv import load_dotenv
from tkinter import *
import PIL
from PIL import Image 


load_dotenv()

def leadgenerate():
    prompt = "Can you give a lists of landscaping business in chicago that I can contact?"
 

    print(prompt)

    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)

def stockgenerate():
    prompt = "Can you give me a lists of stocks that I can invest in 2024?"

    print(prompt)
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)

def relaxdaygenerate():
    prompt = "Can you give me a relaxing schedule day for tuesday?"

    print(prompt)
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)
    


root = ctk.CTk()
root.geometry("750x550")
root.title("ChatGPT Project Idea Generator")

image = PIL.Image.open('Universal4.png')
background_image = ctk.CTkImage(image, size=(1000, 800))

bg_lbl = ctk.CTkLabel(root, text="", image=background_image)
bg_lbl.place(x=0, y=0)

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root, text="Welcome To Universal AI", 
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

frame = ctk.CTkFrame(root, fg_color = 'transparent')
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20,5), fill="both")
language_label = ctk.CTkLabel(
    language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
language_label.pack
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Generate Lead"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=20, pady=10)

features_frame = ctk. CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="More Data")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="Short Answer")
checkbox2.pack(side="left", padx=50, pady=10)

button1 = ctk.CTkButton(frame, text="Generate Leads", command=leadgenerate, fg_color = '#A020F0')
button2 = ctk.CTkButton(frame, text="Stocks", command=stockgenerate, fg_color = '#A020F0' )
button3 = ctk.CTkButton(frame, text="Relax Day", command=relaxdaygenerate, fg_color = '#A020F0')
button1.pack(padx=100, fill="x", pady=(5,20))
button2.pack(padx=100, fill="x", pady=(6,20))
button3.pack(padx=100, fill="x", pady=(7,20))



result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

root.mainloop()