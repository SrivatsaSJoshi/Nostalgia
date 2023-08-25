import os
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, root, csv_path):
        self.root = root
        self.root.title("Image Duplicate Viewer")
        
        self.images = []
        self.current_index = 0
        
        self.load_csv(csv_path)
        
        self.image_label1 = ttk.Label(root)
        self.image_label2 = ttk.Label(root)
        
        self.delete_button1 = ttk.Button(root, text="Delete Image 1", command=self.delete_image1)
        self.delete_button2 = ttk.Button(root, text="Delete Image 2", command=self.delete_image2)
        
        self.show_images()
        
    def load_csv(self, csv_path):
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                self.images.append((row[0], row[1]))
                
    def show_images(self):
        if self.current_index < len(self.images):
            image1_path, image2_path = self.images[self.current_index]
            
            image1 = Image.open(image1_path)
            image2 = Image.open(image2_path)
            
            image1.thumbnail((300, 300))
            image2.thumbnail((300, 300))
            
            photo1 = ImageTk.PhotoImage(image1)
            photo2 = ImageTk.PhotoImage(image2)
            
            self.image_label1.config(image=photo1)
            self.image_label2.config(image=photo2)
            
            self.image_label1.image = photo1
            self.image_label2.image = photo2
            
            self.image_label1.grid(row=0, column=0, padx=10, pady=10)
            self.image_label2.grid(row=0, column=1, padx=10, pady=10)
            
            self.delete_button1.grid(row=1, column=0, padx=10, pady=10)
            self.delete_button2.grid(row=1, column=1, padx=10, pady=10)
            
        else:
            self.image_label1.grid_forget()
            self.image_label2.grid_forget()
            self.delete_button1.grid_forget()
            self.delete_button2.grid_forget()
            
            ttk.Label(self.root, text="No more duplicate pairs").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
    def delete_image1(self):
        self.delete_current_images()
        self.show_images()
        
    def delete_image2(self):
        self.delete_current_images()
        self.show_images()
        
    def delete_current_images(self):
        if self.current_index < len(self.images):
            original_path, duplicate_path = self.images[self.current_index]
            os.remove(original_path)
            os.remove(duplicate_path)
            self.images.pop(self.current_index)
            
root = tk.Tk()
app = ImageDisplayApp(root, "duplicate_images.csv")
root.mainloop()

