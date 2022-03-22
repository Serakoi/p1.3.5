import tkinter as tk
window = tk.Tk()

entry = tk.Entry()

def handle_submit():
    try:
        print("Processing Submission")
        text = entry.get()

        if not text:
            print("No text entered")
            entry.delete(0, tk.END)
            return entry.insert(0,"No text entered!")

        JAAR = int(text)

        MIJN_LEEFTIJD = 2022 - JAAR
        print("Age is:", MIJN_LEEFTIJD)

        entry.delete(0, tk.END)
        entry.insert(0, f"Jouw leeftijd in 2022: {MIJN_LEEFTIJD}")

    except:
        print("Error")
        entry.delete(0, tk.END)
        return entry.insert(0,"Kon data niet parsen!")

def handle_clear():
    entry.delete(0, tk.END)
    return print("CLEARED CONTENT")


label = tk.Label(text="Voeg je geboorte jaar in")
label.pack()
entry.pack()

clear = tk.Button(text="Clear", command=handle_clear)

button = tk.Button(
    text="Submit",
    width=25,
    height=1,
    command=handle_submit
)

clear.pack()
button.pack()

# Run app
window.mainloop()