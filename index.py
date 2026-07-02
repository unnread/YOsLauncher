import customtkinter as ctk
import subprocess

# 🎨 Theme summer
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("YLauncher ☀️ Summer Edition")
app.geometry("420x520")
app.resizable(False, False)

# 🌿 Open apps
def run(app_name):
    subprocess.Popen(app_name)

# 🧊 Main frame
main_frame = ctk.CTkFrame(
    app,
    fg_color="#0f1410",
    corner_radius=24,
    border_width=1,
    border_color="#2ecc71"
)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# 🌞 Title
ctk.CTkLabel(
    main_frame,
    text="☀️ YLauncher",
    font=("Helvetica", 28, "bold"),
    text_color="#a8ffaf"
).pack(pady=(25, 5))

ctk.CTkLabel(
    main_frame,
    text="Summer Edition • apps rapides",
    font=("Helvetica", 13),
    text_color="#c6f3c6"
).pack(pady=(0, 20))

# 🔘 Button style function
def make_btn(text, cmd):
    return ctk.CTkButton(
        main_frame,
        text=text,
        command=cmd,
        fg_color="#1f3d1f",
        hover_color="#2ecc71",
        text_color="white",
        corner_radius=16,
        height=45
    )

# 🚀 Apps
make_btn(" Firefox", lambda: run("firefox")).pack(fill="x", padx=25, pady=6)
make_btn(" VS Code", lambda: run("code")).pack(fill="x", padx=25, pady=6)
make_btn(" Terminal", lambda: run("lxterminal")).pack(fill="x", padx=25, pady=6)

# 🌴 Footer
ctk.CTkLabel(
    main_frame,
    text="v0.1 Summer Build ☀️",
    font=("Helvetica", 11),
    text_color="#6b8f6b"
).pack(side="bottom", pady=15)

app.mainloop()
