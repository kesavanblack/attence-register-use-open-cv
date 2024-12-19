import smtplib
import tkinter as tk
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send emails
def send_emails():
    sender_email = sender_entry.get()
    password = password_entry.get()
    subject = subject_entry.get()
    message_text = message_entry.get("1.0", tk.END)
    recipients = recipient_entry.get("1.0", tk.END).strip().split('\n')
    
    if len(recipients) > 100:
        messagebox.showerror("Error", "You can only send to a maximum of 100 recipients.")
        return
    
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message_text, 'plain'))
            
            # Send the email
            server.sendmail(sender_email, recipient, msg.as_string())
        
        messagebox.showinfo("Success", "Emails sent successfully!")
        server.quit()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setting up the GUI
root = tk.Tk()
root.title("Bulk Email Sender")

tk.Label(root, text="Your Email:").grid(row=0, column=0, padx=10, pady=10)
sender_entry = tk.Entry(root, width=40)
sender_entry.grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=40, show='*')
password_entry.grid(row=1, column=1)

tk.Label(root, text="Recipients (one per line, max 100):").grid(row=2, column=0, padx=10, pady=10)
recipient_entry = tk.Text(root, width=40, height=10)
recipient_entry.grid(row=2, column=1)

tk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=10)
subject_entry = tk.Entry(root, width=40)
subject_entry.grid(row=3, column=1)

tk.Label(root, text="Message:").grid(row=4, column=0, padx=10, pady=10)
message_entry = tk.Text(root, width=40, height=10)
message_entry.grid(row=4, column=1)

send_button = tk.Button(root, text="Send Emails", command=send_emails)
send_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
