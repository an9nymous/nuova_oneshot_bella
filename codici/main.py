import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Negozio:
    def __init__(self, master, nome):
        self.master = master
        self.nome = nome
        self.data = self.initialize_data(nome)
        self.auto_mode = False

        self.root = tk.Toplevel(master)
        self.root.title(f"Negozio di D&D - {self.nome}")

        self.setup_ui()

    def initialize_data(self, nome):
        """Inizializza i dati in base al nome del negozio."""
        if "magia" in nome.lower():
            return {
                "gold": 100,
                "items": {
                    "Pozione di guarigione": {"price": 50, "quantity": 10},
                    "Bacchetta magica": {"price": 75, "quantity": 7},
                    "Elisir di Mana": {"price": 100, "quantity": 5},
                    "Pergamena di Teletrasporto": {"price": 150, "quantity": 3},
                    "Cristallo Magico": {"price": 200, "quantity": 2},
                    "Rune di Protezione": {"price": 250, "quantity": 4},
                    "Amuleto del Magus": {"price": 300, "quantity": 1}
                }
            }
        elif "armi" in nome.lower():
            return {
                "gold": 150,
                "items": {
                    "Spada lunga": {"price": 100, "quantity": 5},
                    "Scudo": {"price": 75, "quantity": 3},
                    "Arco corto": {"price": 150, "quantity": 2},
                    "Ascia da battaglia": {"price": 120, "quantity": 4},
                    "Pugnale": {"price": 80, "quantity": 6},
                    "Lancia": {"price": 90, "quantity": 5},
                    "Martello da guerra": {"price": 200, "quantity": 2}
                }
            }
        elif "cibo" in nome.lower():
            return {
                "gold": 50,
                "items": {
                    "Pane": {"price": 5, "quantity": 20},
                    "Formaggio": {"price": 10, "quantity": 15},
                    "Vino": {"price": 20, "quantity": 10},
                    "Carne essiccata": {"price": 25, "quantity": 8},
                    "Frutta fresca": {"price": 15, "quantity": 12},
                    "Noci": {"price": 8, "quantity": 25},
                    "Cibo da Campo": {"price": 12, "quantity": 18}
                }
            }
        elif "strumenti" in nome.lower():
            return {
                "gold": 80,
                "items": {
                    "Kit da Avventuriero": {"price": 60, "quantity": 5},
                    "Mappa del Tesoro": {"price": 100, "quantity": 3},
                    "Lanterna Magica": {"price": 45, "quantity": 7},
                    "Filo d'Argento": {"price": 25, "quantity": 15},
                    "Campanella di Allerta": {"price": 30, "quantity": 10},
                    "Pozione di Invisibilità": {"price": 200, "quantity": 2}
                }
            }
        elif "generale" in nome.lower():
            return {
                "gold": 200,
                "items": {
                    "Pozione di guarigione": {"price": 50, "quantity": 15},
                    "Spada lunga": {"price": 100, "quantity": 10},
                    "Scudo": {"price": 75, "quantity": 6},
                    "Elisir di Mana": {"price": 100, "quantity": 10},
                    "Mantello dell'invisibilità": {"price": 200, "quantity": 2},
                    "Pane": {"price": 5, "quantity": 20},
                    "Formaggio": {"price": 10, "quantity": 15},
                    "Kit da Avventuriero": {"price": 60, "quantity": 5},
                    "Mappa del Tesoro": {"price": 100, "quantity": 3}
                }
            }
        else:
            return {
                "gold": 100,
                "items": {
                    "Pozione di guarigione": {"price": 50, "quantity": 10},
                    "Spada lunga": {"price": 100, "quantity": 5},
                    "Scudo": {"price": 75, "quantity": 3},
                    "Arco corto": {"price": 150, "quantity": 2},
                    "Mantello dell'invisibilità": {"price": 200, "quantity": 1},
                    "Pane": {"price": 5, "quantity": 20},
                    "Formaggio": {"price": 10, "quantity": 15}
                }
            }

    def setup_ui(self):
        """Configura l'interfaccia utente del negozio."""
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

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
            if self.data['gold'] >= amount:
                self.data['gold'] -= amount
                self.update_ui()
            else:
                messagebox.showerror("Errore", "Oro insufficiente")
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero valido")

    def buy_item(self, item):
        """Acquista un oggetto."""
        if self.data['gold'] >= self.data['items'][item]['price']:
            self.data['gold'] -= self.data['items'][item]['price']
            self.data['items'][item]['quantity'] += 1
            self.update_ui()
        else:
            messagebox.showerror("Errore", "Oro insufficiente")

    def sell_item(self, item):
        """Vendi un oggetto."""
        if self.data['items'][item]['quantity'] > 0:
            self.data['gold'] += self.data['items'][item]['price']
            self.data['items'][item]['quantity'] -= 1
            self.update_ui()
        else:
            messagebox.showerror("Errore", "Quantità insufficiente")

    def automatic_update(self):
        """Aggiornamento automatico dei dati."""
        if self.auto_mode:
            self.data['gold'] += random.randint(-20, 50)
            for item in self.data['items']:
                change = random.randint(-3, 3)
                self.data['items'][item]['quantity'] = max(0, self.data['items'][item]['quantity'] + change)
            self.update_ui()
            N = random.randint(5, 15)
            self.root.after(N * 1000, self.automatic_update)

    def toggle_mode(self):
        """Passa tra modalità manuale e automatica."""
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.mode_button.config(text="Passa a Manuale")
            self.automatic_update()
        else:
            self.mode_button.config(text="Passa ad Automatico")


class PannelloDiComando:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pannello di Comando")

        self.negozi = {}

        self.new_negozio_button = tk.Button(self.root, text="Crea Nuovo Negozio", command=self.crea_negozio)
        self.new_negozio_button.pack(pady=10)

        self.root.mainloop()

    def crea_negozio(self):
        """Crea un nuovo negozio con un nome unico."""
        nome = simpledialog.askstring("Nome del Negozio", "Inserisci il nome del nuovo negozio:", parent=self.root)
        if nome:
            if nome in self.negozi:
                messagebox.showerror("Errore", "Esiste già un negozio con questo nome.")
            else:
                negozio = Negozio(self.root, nome)
                self.negozi[nome] = negozio


if __name__ == "__main__":
    PannelloDiComando()
