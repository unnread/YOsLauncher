import customtkinter as ctk
import subprocess

# en = You can change if you dont have vscode or firefox or lxterminal ..lalal
# fr = Tu peux changer si tu as pas vscode ou firefox ou lxterminal ... etc

def add():
    subprocess.Popen("firefox")

def add1():
    subprocess.Popen("code")

def add2():
    subprocess.Popen("lxterminal")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()

app.title("Mon App")
app.geometry("420x520")
app.resizable(False, False)

main_frame = ctk.CTkFrame(
    app,
    fg_color="#111318",
    corner_radius=24,
    border_width=1,
    border_color="#1f5c1f",
)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

label = ctk.CTkLabel(
    main_frame,
    text="Welcome",
    font=("Helvetica", 26, "bold"),
    text_color="#a8ffaf",
)
label.pack(pady=(24, 8))

subtitle = ctk.CTkLabel(
    main_frame,
    text="Choisis une action ci-dessous",
    font=("Helvetica", 14),
    text_color="#c6f3c6",
)
subtitle.pack(pady=(0, 24))

btn = ctk.CTkButton(
    main_frame,
    text="Ouvrir Firefox",
    command=add,
    fg_color="#285228",
    hover_color="#2f6b2f",
    text_color="white",
    corner_radius=18,
    border_width=0,
    height=48,
)
btn.pack(fill="x", padx=24, pady=(0, 12))

btn1 = ctk.CTkButton(
    main_frame,
    text="Ouvrir VS Code",
    command=add1,
    fg_color="#285228",
    hover_color="#2f6b2f",
    text_color="white",
    corner_radius=18,
    border_width=0,
    height=48,
)
btn1.pack(fill="x", padx=24, pady=(0, 12))

btn2 = ctk.CTkButton(
    main_frame,
    text="Ouvrir Terminal",
    command=add2,
    fg_color="#285228",
    hover_color="#2f6b2f",
    text_color="white",
    corner_radius=18,
    border_width=0,
    height=48,
)
btn2.pack(fill="x", padx=24, pady=(0, 24))

footer = ctk.CTkLabel(
    main_frame,
    text="Version 0 (Sa sera la première et La DERNIÈRE)",
    font=("Helvetica", 11),
   text_color="#6b8f6b",
)
footer.pack(side="bottom", pady=12)

app.mainloop()
