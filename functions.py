from tkinter import Button, HIDDEN, NORMAL, DISABLED

class Functions:
    aux_button = Button()
    def updateStats(self, stats, canvas, db):
        canvas.itemconfig(stats['atk'], text = db.character['stats']['atk'])
        canvas.itemconfig(stats['def'], text = db.character['stats']['def'])
        canvas.itemconfig(stats['vel'], text = db.character['stats']['vel'])
        canvas.itemconfig(stats['mag'], text = db.character['stats']['mag'])

    def inventory_sheet_button(self, buttons, db, coords, inventory_items, section, background, canvas, img):
        canvas.itemconfig(background, image = img)
        
        buttons['helmets_section'].place(x = 2, y = 5)
        buttons['boots_section'].place(x = 332, y = 7)
        buttons['pants_section'].place(x = 221, y = 7)
        buttons['chestplates_section'].place(x = 110, y = 7)
        buttons['weapons_section'].place(x = 582, y = 6)
        buttons['artifacts_section'].place(x = 693, y = 7)
        buttons['equip_B'].place(x = 31, y = 571)
        buttons['unequip_B'].place(x = 205, y = 571)
        buttons['info_B'].place(x = 379, y = 571)
        buttons['back_B'].place(x = 553, y = 571)

        buttons[section].place_forget()

        for item in inventory_items:
            inventory_items[item].place_forget()

        try:
            if(section == 'helmets_section'):
                for i, item in enumerate(coords):
                    inventory_items[db.helmets[i]['code']].place(x = item[0], y = item[1])
            elif(section == 'chestplates_section'):
                for i, item in enumerate(coords):
                    inventory_items[db.chestplates[i]['code']].place(x = item[0], y = item[1])
            elif(section == 'pants_section'):
                for i, item in enumerate(coords):
                    inventory_items[db.pants[i]['code']].place(x = item[0], y = item[1])
            elif(section == 'boots_section'):
                for i, item in enumerate(coords):
                    inventory_items[db.boots[i]['code']].place(x = item[0], y = item[1])
            elif(section == 'weapons_section'):
                for i, item in enumerate(coords):
                    inventory_items[db.weapons[i]['code']].place(x = item[0], y = item[1])
            elif(section == 'artifacts_section'):
                for i, item in enumerate(coords):
                    inventory_items[db.artifacts[i]['code']].place(x = item[0], y = item[1])
        except:
            next
    
    def initialize_inventory_sheet(self, root, db, background, canvas, img, stats_text, buttons, inventory_items, coords, section):
        root.geometry("800x671")
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

        self.inventory_sheet_button(buttons, db, coords, inventory_items, section, background, canvas, img)

    def initialize_character_sheet(self, root, background, canvas, img, buttons, stats_text, inventory_items):
        root.geometry("800x800")
        canvas.itemconfig(background, image = img)
        buttons['helmets_section'].place_forget()
        buttons['boots_section'].place_forget()
        buttons['pants_section'].place_forget()
        buttons['chestplates_section'].place_forget()
        buttons['weapons_section'].place_forget()
        buttons['artifacts_section'].place_forget()
        buttons['equip_B'].place_forget()
        buttons['unequip_B'].place_forget()
        buttons['info_B'].place_forget()
        buttons['back_B'].place_forget()
        for item in inventory_items:
            inventory_items[item].place_forget()

        canvas.itemconfig(stats_text['atk'], state= NORMAL)
        canvas.itemconfig(stats_text['def'], state= NORMAL)
        canvas.itemconfig(stats_text['vel'], state= NORMAL)
        canvas.itemconfig(stats_text['mag'], state= NORMAL)

        buttons['helmet_B'].place(x = 162, y = 226)
        buttons['chestplate_B'].place(x = 523, y = 224)
        buttons['pants_B'].place(x = 162, y = 355)
        buttons['boots_B'].place(x = 523, y = 355)
        buttons['weapon_B'].place(x = 268, y = 87)
        buttons['artifact_B'].place(x = 417, y = 87)

    def select_item(self, button, character_armor, piece):
        character_armor[piece]['state'] = NORMAL
        character_armor[piece] = button
        character_armor[piece]['state'] = DISABLED

    def btn(self):
        a = 0