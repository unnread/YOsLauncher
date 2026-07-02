import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("YLauncher Summer")
app.geometry("420x520")
app.resizable(False, False)

def run(cmd):
    subprocess.Popen(cmd)

# 🌊 Frame été
main_frame = ctk.CTkFrame(
    app,
    fg_color="#1a2a2f",   # océan sombre
    corner_radius=25,
    border_width=2,
    border_color="#ffcc70"  # soleil
)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# ☀️ Title
ctk.CTkLabel(
    main_frame,
    text=" Summer Launcher",
    font=("Helvetica", 28, "bold"),
    text_color="#ffd36e"
).pack(pady=(25, 5))

ctk.CTkLabel(
    main_frame,
    text="Mise a Jour ...   Summer !",
    font=("Helvetica", 13),
    text_color="#8fd3ff"
).pack(pady=(0, 20))

# 🔘 bouton style été
def make_btn(text, cmd):
    return ctk.CTkButton(
        main_frame,
        text=text,
        command=cmd,
        fg_color="#24545f",  
        hover_color="#ffcc70",
        text_color="white",
        corner_radius=16,
        height=45,
        border_width=0
    )

#  Apps
make_btn(" Firefox", lambda: run("firefox")).pack(fill="x", padx=25, pady=6)
make_btn(" VS Code", lambda: run("code")).pack(fill="x", padx=25, pady=6)
make_btn(" Terminal", lambda: run("lxterminal")).pack(fill="x", padx=25, pady=6)

#  Footer
ctk.CTkLabel(
    main_frame,
    text="v0.1 Summer Build ☀️",
    font=("Helvetica", 11),
    text_color="#8fd3ff"
).pack(side="bottom", pady=15)

app.mainloop()
