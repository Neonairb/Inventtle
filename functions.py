from tkinter import Button, HIDDEN

class Functions:
    def createButton(self, x, y, width, height, func, img):
        button = Button(
            image = img,
            borderwidth = 0,
            highlightthickness = 0,
            command = func,
            relief = "flat")
        button.place(x=x, y=y, width=width, height=height)
        
        return button
        
    def updateStats(self, stats, canvas, db):
        canvas.itemconfig(stats['atk'], text = db.character['stats']['atk'])
        canvas.itemconfig(stats['def'], text = db.character['stats']['def'])
        canvas.itemconfig(stats['vel'], text = db.character['stats']['vel'])
        canvas.itemconfig(stats['mag'], text = db.character['stats']['mag'])

    def helmet_BA(self, root, background, canvas, img, buttons, stats_text):
        self.initialize_inventory(root, background, canvas, img, buttons, stats_text)

        buttons['helmets_section'].place_forget()

    def chestplate_BA(self, root, background, canvas, img, buttons, stats_text):
        self.initialize_inventory(root, background, canvas, img, buttons, stats_text)

        buttons['chestplates_section'].place_forget()

    def pant_BA(self, root, background, canvas, img, buttons, stats_text):
        self.initialize_inventory(root, background, canvas, img, buttons, stats_text)

        buttons['pants_section'].place_forget()

    def boot_BA(self, root, background, canvas, img, buttons, stats_text):
        self.initialize_inventory(root, background, canvas, img, buttons, stats_text)

        buttons['boots_section'].place_forget()

    def weapon_BA(self, root, background, canvas, img, buttons, stats_text):
        self.initialize_inventory(root, background, canvas, img, buttons, stats_text)

        buttons['weapons_section'].place_forget()

    def artifact_BA(self, root, background, canvas, img, buttons, stats_text):
        self.initialize_inventory(root, background, canvas, img, buttons, stats_text)

        buttons['artifacts_section'].place_forget()
    
    def initialize_inventory(self, root, background, canvas, img, buttons, stats_text):
        root.geometry("800x671")
        canvas.itemconfig(background, image = img)
        buttons['helmet_B'].place_forget()
        buttons['chestplate_B'].place_forget()
        buttons['pants_B'].place_forget()
        buttons['boots_B'].place_forget()
        buttons['weapon_B'].place_forget()
        buttons['artifact_B'].place_forget()

        canvas.itemconfig(stats_text['atk'], state= HIDDEN)
        canvas.itemconfig(stats_text['def'], state= HIDDEN)
        canvas.itemconfig(stats_text['vel'], state= HIDDEN)
        canvas.itemconfig(stats_text['mag'], state= HIDDEN)

        buttons['helmets_section'].place(x = 2, y = 5)
        buttons['boots_section'].place(x = 332, y = 7)
        buttons['pants_section'].place(x = 221, y = 7)
        buttons['chestplates_section'].place(x = 110, y = 7)
        buttons['weapons_section'].place(x = 582, y = 6)
        buttons['artifacts_section'].place(x = 693, y = 7)
        buttons['equip_B'].place(x = 31, y = 571)
        buttons['unequip_B'].place(x = 205, y = 571),
        buttons['info_B'].place(x = 379, y = 571),
        buttons['back_B'].place(x = 553, y = 571)

    def btn(self):
        a = 0