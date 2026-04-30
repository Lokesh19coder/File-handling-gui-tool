import tkinter as tk
from tkinter import messagebox, filedialog
import re

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def modify_file():
    filename = file_entry.get()
    find_word = find_entry.get()
    replace_word = replace_entry.get()
    ignore_case = case_var.get()

    if not filename or not find_word:
        messagebox.showwarning("Warning", "Please fill all required fields!")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Replace logic
        if ignore_case:
            modified_content, count = re.subn(find_word, replace_word, content, flags=re.IGNORECASE)
        else:
            count = content.count(find_word)
            modified_content = content.replace(find_word, replace_word)

        with open(filename, 'w') as file:
            file.write(modified_content)

        # Show result
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, modified_content)

        messagebox.showinfo("Success", f"File updated!\nReplacements made: {count}")

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")

    except PermissionError:
        messagebox.showerror("Error", "Permission denied!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_output():
    result_text.delete(1.0, tk.END)


# --- GUI Setup ---
root = tk.Tk()
root.title("Advanced File Handler Tool")
root.geometry("600x500")
root.configure(bg="#1e1e1e")  # Dark mode

# --- Title ---
tk.Label(root, text="File Handling Tool", font=("Arial", 16, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

# --- File Input ---
frame_file = tk.Frame(root, bg="#1e1e1e")
frame_file.pack(pady=5)

file_entry = tk.Entry(frame_file, width=40)
file_entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame_file, text="Browse", command=browse_file,
          bg="#007acc", fg="white").pack(side=tk.LEFT)

# --- Find Word ---
tk.Label(root, text="Find Word", bg="#1e1e1e", fg="white").pack()
find_entry = tk.Entry(root, width=40)
find_entry.pack(pady=5)

# --- Replace Word ---
tk.Label(root, text="Replace With", bg="#1e1e1e", fg="white").pack()
replace_entry = tk.Entry(root, width=40)
replace_entry.pack(pady=5)

# --- Case Option ---
case_var = tk.IntVar()
tk.Checkbutton(root, text="Ignore Case",
               variable=case_var, bg="#1e1e1e", fg="white",
               selectcolor="#1e1e1e").pack()

# --- Buttons ---
tk.Button(root, text="Modify File", command=modify_file,
          bg="#28a745", fg="white", width=20).pack(pady=10)

tk.Button(root, text="Clear Output", command=clear_output,
          bg="#dc3545", fg="white", width=20).pack()

# --- Output Box ---
result_text = tk.Text(root, height=12, width=70, bg="#2d2d2d", fg="white")
result_text.pack(pady=10)

# --- Run App ---
root.mainloop()