import customtkinter as ctk

# Initialize the CustomTkinter app
app = ctk.CTk()

# Set window size
app.geometry("500x500")
app.title("Bank Login")

# Set theme and appearance mode
ctk.set_appearance_mode("System")

# Add the "Login to the Bank" label
title_label = ctk.CTkLabel(master=app, text="Login to the Bank", font=("Arial", 24))
title_label.pack(pady=20)

# Add widgets for ID
id_label = ctk.CTkLabel(master=app, text="ID:")
id_label.pack(pady=5)
id_entry = ctk.CTkEntry(master=app, width=200)
id_entry.pack(pady=5)

# Add widgets for Password
password_label = ctk.CTkLabel(master=app, text="Password:")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(master=app, width=200, show="*")  # show="*" hides the password
password_entry.pack(pady=5)


def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')  # Show the password
        show_password_button.configure(text='Hide Password')
    else:
        password_entry.configure(show='*')  # Hide the password
        show_password_button.configure(text='Show Password')


# Add a "Show Password" button
show_password_button = ctk.CTkButton(master=app, text="Show Password", command=toggle_password, fg_color="gray",
                                     hover_color="darkgray")
show_password_button.pack(pady=5)
# Add buttons for Login and Sign Up

login_button = ctk.CTkButton(master=app, text="Login", command=lambda: print("Login pressed"))
login_button.pack(pady=50)

signup_label = ctk.CTkLabel(master=app, text="Don't have an account?", font=("Arial", 18))
signup_label.pack()

signup_button = ctk.CTkButton(master=app, text="Sign Up", command=lambda: print("Sign Up pressed"))
signup_button.pack()

# Run the application
app.mainloop()
