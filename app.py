import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup as bs
import requests


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Web Scraper")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.configure(background="#F5F5F5")

        self.url_label = tk.Label(
            self.root, text="Enter Url: ", bg="#F5F5F5", fg="#333333"
        )
        self.url_label.pack(padx=5, pady=5)

        self.url_entry = tk.Entry(self.root, width=50, bg="#F5F5F5", fg="#333333")
        self.url_entry.pack(padx=5, pady=5)

        self.word_label = tk.Label(
            self.root, text="Enter a Word to Find: ", bg="#F5F5F5", fg="#333333"
        )
        self.word_label.pack(padx=5, pady=5)

        self.word_entry = tk.Entry(self.root, width=50, bg="#F5F5F5", fg="#333333")
        self.word_entry.pack(padx=5, pady=5)

        self.scrape_btn = tk.Button(
            self.root,
            text="Scrape Data",
            command=self.scrape_data,
            bg="#007BFF",
            fg="#FFFFFF",
        )
        self.scrape_btn.pack(padx=5, pady=5)

        self.search_words = [self.word_entry.get()]

    def scrape_data(self):
        url = self.url_entry.get()
        r = requests.get(url)
        r.raise_for_status()
        soup = bs(r.content, "html.parser")

        source_text = soup.get_text().lower()
        word_to_find = self.word_entry.get().lower()
        found_words = []

        if word_to_find in source_text:
            found_words.append(word_to_find)

        messagebox.showinfo(f"Scraped Data", f"Scraped Data: {found_words}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
