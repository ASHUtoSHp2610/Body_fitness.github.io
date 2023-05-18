import tkinter as tk

users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def forgot_password():
    username = username_entry.get()
    
    if username in users:
        new_password = new_password_entry.get()
        users[username] = new_password
        result_label.config(text="Password updated successfully.", fg="green")
    else:
        result_label.config(text="Username not found.", fg="red")

# Create the window
window = tk.Tk()
window.title("Forgot Password")
window.geometry("300x150")

# Create the username label and entry
username_label = tk.Label(window, text="Enter your username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Create the new password label and entry
new_password_label = tk.Label(window, text="Enter a new password:")
new_password_label.pack()
new_password_entry = tk.Entry(window)
new_password_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=forgot_password)
submit_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the window loop
window.mainloop()