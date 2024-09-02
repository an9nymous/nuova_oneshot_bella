import tkinter as tk
from tkinter import messagebox, ttk
import random

class Negozio:
    def __init__(self, master, nome, tipo_merce):
        self.master = master
        self.nome = nome
        self.tipo_merce = tipo_merce
        self.data = self.initialize_data(tipo_merce)
        self.auto_mode = False
        self.min_gold_threshold = 50  # Soglia minima di oro

        self.root = tk.Toplevel(master)
        self.root.title(f"{self.nome} - {self.tipo_merce.capitalize()}")

        self.setup_ui()

    def initialize_data(self, tipo_merce):
        """Inizializza i dati in base al tipo di merce del negozio."""
        data = {
            "magia": {
                "gold": 100,
                "items": {
                    "Pozione di guarigione": {"price": 50, "quantity": 10},
                    "Bacchetta magica": {"price": 15, "quantity": 7},
                    "Pergamena di Teletrasporto": {"price": 150, "quantity": 3},
                    "Cristallo Magico": {"price": 10, "quantity": 2},
                    "Rune di Protezione": {"price": 250, "quantity": 4},
                }
            },
            "armi": {
                "gold": 150,
                "items": {
                    "Spada lunga": {"price": 16, "quantity": 5},
                    "Scudo": {"price": 11, "quantity": 3},
                    "Arco corto": {"price": 26, "quantity": 2},
                    "Ascia da battaglia": {"price": 11, "quantity": 4},
                    "Pugnale": {"price": 3, "quantity": 6},
                    "Lancia": {"price": 2, "quantity": 5},
                    "Martello da guerra": {"price": 16, "quantity": 2},
                    "ascia bipenne":{"price": 31, "quantity": 2}
                }
            },
            "cibo": {
                "gold": 50,
                "items": {
                    "Pane": {"price": 1, "quantity": 10},
                    "Formaggio": {"price": 10, "quantity": 15},
                    "Vino": {"price": 20, "quantity": 10},
                    "Carne essiccata": {"price": 25, "quantity": 8},
                    "Frutta fresca": {"price": 15, "quantity": 12},
                    "Noci": {"price": 8, "quantity": 25},
                    "razioni giornaliere": {"price": 12, "quantity": 18}
                }
            },
            "strumenti": {
                "gold": 80,
                "items": {
                    "strumenti da pittore": {"price": 20, "quantity": 5},
                    "Mappa del Tesoro": {"price": 100, "quantity": 3},
                    "Lanterna Magica": {"price": 45, "quantity": 7},
                    "viola": {"price": 30, "quantity": 1},
                    "giaciglio": {"price": 1, "quantity": 10}
                }
            },
            "generale": {
                "gold": 200,
                "items": {
                    "Pozione di guarigione": {"price": 50, "quantity": 15},
                    "Spada lunga": {"price": 20, "quantity": 10},
                    "Scudo": {"price": 30, "quantity": 6},
                    "Pane": {"price": 5, "quantity": 20},
                    "Formaggio": {"price": 10, "quantity": 15},
                    "strumenti da alchimista": {"price": 60, "quantity": 5},
                    "Mappa del Tesoro": {"price": 100, "quantity": 3}
                }
            },
            "veicoli":{
                "gold": 200,
                "items":{
                    "mulo":{"price": 8, "quantity":10},
                    "cavallo": {"price": 75, "quantity": 5},
                    "cavallo da guerra": {"price": 400, "quantity": 3},
                    "barca a remi": {"price": 50, "quantity": 2}
                }
            }
        }

        return data.get(tipo_merce, {
            "gold": 100,
            "items": {
                "Pozione di guarigione": {"price": 50, "quantity": 10},
                "Spada lunga": {"price": 17, "quantity": 5},
                "Scudo": {"price": 25, "quantity": 3},
                "Arco corto": {"price": 30, "quantity": 2},
                "Pane": {"price": 5, "quantity": 20},
                "Formaggio": {"price": 10, "quantity": 15}
            }
        })

    def setup_ui(self):
        """Configura l'interfaccia utente del negozio."""
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Label per mostrare il nome del negozio e il tipo di merce come titolo
        titolo_label = tk.Label(main_frame, text=f"{self.nome} - {self.tipo_merce.capitalize()}", font=('Arial', 18, 'bold'))
        titolo_label.pack(pady=10)

        # Label per mostrare l'oro disponibile
        self.gold_label = tk.Label(main_frame, text=f"Oro disponibile: {self.data['gold']}", font=('Arial', 16))
        self.gold_label.pack(pady=10)

        # Entry per l'input dell'oro
        self.gold_entry = tk.Entry(main_frame)
        self.gold_entry.pack(pady=5)

        # Bottoni per aggiungere e rimuovere oro
        self.add_gold_button = tk.Button(main_frame, text="Aggiungi Oro", command=self.add_gold)
        self.add_gold_button.pack(side=tk.LEFT, padx=5)

        self.remove_gold_button = tk.Button(main_frame, text="Rimuovi Oro", command=self.remove_gold)
        self.remove_gold_button.pack(side=tk.LEFT, padx=5)

        # Bottone per cambiare modalità
        self.mode_button = tk.Button(main_frame, text="Passa ad Automatico", command=self.toggle_mode)
        self.mode_button.pack(pady=10)

        # Frame per gli oggetti
        items_frame = tk.Frame(main_frame)
        items_frame.pack(fill=tk.BOTH, expand=True)

        # Dizionario per tenere traccia delle label degli oggetti
        self.item_labels = {}

        # Crea le sezioni per ogni oggetto
        for item, details in self.data['items'].items():
            item_frame = tk.Frame(items_frame, padx=10, pady=5)
            item_frame.pack(fill=tk.X)

            item_name_label = tk.Label(item_frame, text=item, font=('Arial', 12))
            item_name_label.grid(row=0, column=0, columnspan=2, sticky='w')

            self.item_labels[item] = {
                "quantity": tk.Label(item_frame, text=f"Quantità: {details['quantity']}", font=('Arial', 10)),
                "price": tk.Label(item_frame, text=f"Prezzo: {details['price']}", font=('Arial', 10))
            }

            self.item_labels[item]['quantity'].grid(row=1, column=0)
            self.item_labels[item]['price'].grid(row=1, column=1)

            buy_button = tk.Button(item_frame, text="Compra", command=lambda i=item: self.buy_item(i))
            buy_button.grid(row=2, column=0, padx=5, pady=5)

            sell_button = tk.Button(item_frame, text="Vendi", command=lambda i=item: self.sell_item(i))
            sell_button.grid(row=2, column=1, padx=5, pady=5)

        # Casella per scrivere note
        self.notes_label = tk.Label(main_frame, text="Note:", font=('Arial', 12))
        self.notes_label.pack(pady=5)

        self.notes_text = tk.Text(main_frame, height=5, width=25)
        self.notes_text.pack(pady=5)

        self.update_ui()

    def update_ui(self):
        """Aggiorna l'interfaccia utente con i dati correnti."""
        self.gold_label.config(text=f"Oro disponibile: {self.data['gold']}")
        for item, details in self.data['items'].items():
            self.item_labels[item]['quantity'].config(text=f"Quantità: {details['quantity']}")
            self.item_labels[item]['price'].config(text=f"Prezzo: {details['price']}")

    def add_gold(self):
        """Aggiungi oro al negozio."""
        try:
            amount = int(self.gold_entry.get())
            self.data['gold'] += amount
            self.update_ui()
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero valido")

    def remove_gold(self):
        """Rimuovi oro dal negozio."""
        try:
            amount = int(self.gold_entry.get())
            if amount <= self.data['gold']:
                self.data['gold'] -= amount
                self.update_ui()
            else:
                messagebox.showerror("Errore", "Oro insufficiente")
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero valido")

    def buy_item(self, item):
        """Compra un oggetto dal negozio."""
        item_details = self.data['items'][item]
        if self.data['gold'] >= item_details['price']:
            self.data['gold'] -= item_details['price']
            item_details['quantity'] += 1
            self.update_ui()
        else:
            messagebox.showerror("Errore", "Non hai abbastanza oro")

    def sell_item(self, item):
        """Vendi un oggetto dal negozio."""
        item_details = self.data['items'][item]
        if item_details['quantity'] > 0:
            # Vendi solo se l'oro è inferiore alla soglia minima
            if self.data['gold'] < self.min_gold_threshold:
                self.data['gold'] += item_details['price']
                item_details['quantity'] -= 1
                self.update_ui()
                # Vendi finché l'oro non raggiunge la soglia minima
                if self.data['gold'] < self.min_gold_threshold:
                    self.root.after(1000, lambda: self.sell_item(item))
            else:
                messagebox.showinfo("Info", "L'oro è sufficiente, puoi acquistare ulteriori beni.")
        else:
            messagebox.showerror("Errore", "Non ci sono abbastanza oggetti")

    def toggle_mode(self):
        """Cambia modalità tra manuale e automatico."""
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.mode_button.config(text="Passa a Manuale")
            self.automatic_update()
        else:
            self.mode_button.config(text="Passa ad Automatico")

    def automatic_update(self):
        """Aggiornamento automatico dei dati."""
        if self.auto_mode:
            self.data['gold'] += random.randint(-20, 50)
            for item in self.data['items']:
                change = random.randint(-3, 3)
                new_quantity = max(1, self.data['items'][item]['quantity'] + change)
                self.data['items'][item]['quantity'] = new_quantity
            self.update_ui()
            self.root.after(5000, self.automatic_update)


class PannelloComando:
    def __init__(self, master):
        self.master = master
        self.master.title("Pannello di Comando")

        # Lista dei tipi di merce
        self.tipi_merce = ["magia", "armi", "cibo", "strumenti", "generale", "veicoli"]

        # Etichetta per il nome del negozio
        self.nome_label = tk.Label(master, text="Nome del Negozio:")
        self.nome_label.pack(pady=10)

        # Entry per il nome del negozio
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack(pady=5)

        # Etichetta per il tipo di merce
        self.tipo_merce_label = tk.Label(master, text="Tipo di Merce:")
        self.tipo_merce_label.pack(pady=10)

        # Dropdown per selezionare il tipo di merce
        self.tipo_merce_combobox = ttk.Combobox(master, values=self.tipi_merce)
        self.tipo_merce_combobox.set(self.tipi_merce[0])
        self.tipo_merce_combobox.pack(pady=5)

        # Bottone per creare il negozio
        self.crea_negozio_button = tk.Button(master, text="Crea Negozio", command=self.crea_negozio)
        self.crea_negozio_button.pack(pady=10)

    def crea_negozio(self):
        nome_negozio = self.nome_entry.get()
        tipo_merce = self.tipo_merce_combobox.get()

        if nome_negozio and tipo_merce:
            Negozio(self.master, nome_negozio, tipo_merce)
        else:
            messagebox.showerror("Errore", "Inserisci il nome del negozio e seleziona il tipo di merce")


if __name__ == "__main__":
    root = tk.Tk()
    pannello = PannelloComando(root)
    root.mainloop()
