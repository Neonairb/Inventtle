from tkinter import Button, Canvas, PhotoImage, DISABLED
from functions import Functions
from database import DataBase

class GUI:
    images = {
    "character_bg":         PhotoImage(file = f"images\character_sheet\character_bg.png"),
    "equipment_frame":      PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    
    "artifacts_bg":         PhotoImage(file = f"images\inventory_sheet\\artifacts_bg.png"),
    "artifacts_section":    PhotoImage(file = f"images\inventory_sheet\\artifacts_section.png"),
    "boots_bg":             PhotoImage(file = f"images\inventory_sheet\\boots_bg.png"),
    "boots_section":        PhotoImage(file = f"images\inventory_sheet\\boots_section.png"),
    "chestplates_bg":       PhotoImage(file = f"images\inventory_sheet\\chestplates_bg.png"),
    "chestplates_section":  PhotoImage(file = f"images\inventory_sheet\\chestplates_section.png"),
    "helmets_bg":           PhotoImage(file = f"images\inventory_sheet\\helmets_bg.png"),
    "helmets_section":      PhotoImage(file = f"images\inventory_sheet\\helmets_section.png"),
    "pants_bg":             PhotoImage(file = f"images\inventory_sheet\\pants_bg.png"),
    "pants_section":        PhotoImage(file = f"images\inventory_sheet\\pants_section.png"),
    "weapons_bg":           PhotoImage(file = f"images\inventory_sheet\\weapons_bg.png"),
    "weapons_section":      PhotoImage(file = f"images\inventory_sheet\\weapons_section.png"),

    "highligt":             PhotoImage(file = f"images\inventory_sheet\\highlight.png"),
    "equip_B":              PhotoImage(file = f"images\inventory_sheet\\equip_B.png"),
    "unequip_B":            PhotoImage(file = f"images\inventory_sheet\\unequip_B.png"),
    "info_B":               PhotoImage(file = f"images\inventory_sheet\\info_B.png"),
    "back_B":               PhotoImage(file = f"images\inventory_sheet\\back_B.png"),
    "e_button":             PhotoImage(file = f"images\inventory_sheet\\e_button.png"),

    "DBM":                  PhotoImage(file = f"images\items\\DBM.png"),
    "DCM":                  PhotoImage(file = f"images\items\\DCM.png"),
    "DHM":                  PhotoImage(file = f"images\items\\DHM.png"),
    "DPM":                  PhotoImage(file = f"images\items\\DPM.png"),
    "DSM":                  PhotoImage(file = f"images\items\\DSM.png"),
    "TOUM":                 PhotoImage(file = f"images\items\\TOUM.png"),
    "WSM":                  PhotoImage(file = f"images\items\\WDM.png"),
    "":                     PhotoImage(file = f"images\items\\empty.png")
    }
    def __init__(self, root):
        root.geometry("800x800")
        root.configure(bg = "#0c0c7b")

        functions = Functions()

        canvas = Canvas(
            root,
            bg = "#0c0c7b",
            height = 800,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background = canvas.create_image(
            0, 0,
            anchor = 'nw',
            image= self.images["character_bg"])

        root = root
        db = DataBase()

        # Texto de las stats
        stats_text = {
            'atk': canvas.create_text(
                    269.5, 620.0,
                    text = db.character['stats']['atk'],
                    fill = "#f8f8f5",
                    font = ("Final Fantasy VII", int(80.0))),
            'mag': canvas.create_text(
                    594.5, 715.0,
                    text = db.character['stats']['mag'],
                    fill = "#f8f8f5",
                    font = ("Final Fantasy VII", int(80.0))),
            'vel': canvas.create_text(
                    594.5, 620.0,
                    text = db.character['stats']['vel'],
                    fill = "#f8f8f5",
                    font = ("Final Fantasy VII", int(80.0))),
            'def': canvas.create_text(
                    269.5, 715.0,
                    text = db.character['stats']['def'],
                    fill = "#f8f8f5",
                    font = ("Final Fantasy VII", int(80.0)))
        }

        # Botones
        coords = []
        y = 114
        for i in range(max(len(db.helmets), len(db.chestplates), len(db.pants), len(db.boots), len(db.weapons), len(db.artifacts))):
            if(i%9 == 0):
                y += 74
            coords.append([37+(74*(i%9)), y])

        inventory_items = {}

        for item in db.helmets:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'helmets_section', stats_text, db.data, code))
        for item in db.chestplates:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'chestplates_section', stats_text, db.data, code))
        for item in db.pants:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'pants_section', stats_text, db.data, code))
        for item in db.boots:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'boots_section', stats_text, db.data, code))
        for item in db.weapons:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'weapons_section', stats_text, db.data, code))
        for item in db.artifacts:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'artifacts_section', stats_text, db.data, code))

        # Equipment of the character
        character_armor = {'helmets_section':       [inventory_items[db.character['armor']['helmet']], db.character['armor']['helmet']], 
                            'chestplates_section':  [inventory_items[db.character['armor']['chestplate']], db.character['armor']['chestplate']], 
                            'pants_section':        [inventory_items[db.character['armor']['pants']], db.character['armor']['pants']], 
                            'boots_section':        [inventory_items[db.character['armor']['boots']], db.character['armor']['boots']], 
                            'weapons_section':      [inventory_items[db.character['weapon']], db.character['weapon']], 
                            'artifacts_section':    [inventory_items[db.character['artifact']], db.character['artifact']]}
        for item in character_armor:
            character_armor[item][0]['state'] = DISABLED

        buttons = {}

        buttons['helmet_B'] = Button(
            image = self.images["equipment_frame"],
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['helmets_bg'], stats_text, buttons, inventory_items, coords, 'helmets_section', character_armor),
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")
        buttons['helmet_B'].place(x = 162, y = 226)

        buttons['chestplate_B'] = Button(
            image = self.images["equipment_frame"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['chestplates_bg'], stats_text, buttons, inventory_items, coords, 'chestplates_section', character_armor),
            relief = "flat")
        buttons['chestplate_B'].place(x = 523, y = 224)
        
        buttons['pants_B'] = Button(
            image = self.images["equipment_frame"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['pants_bg'], stats_text, buttons, inventory_items, coords, 'pants_section', character_armor),
            relief = "flat")
        buttons['pants_B'].place(x = 162, y = 355)
        
        buttons['boots_B'] = Button(
            image = self.images["equipment_frame"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['boots_bg'], stats_text, buttons, inventory_items, coords, 'boots_section', character_armor),
            relief = "flat")
        buttons['boots_B'].place(x = 523, y = 355)
        
        buttons['weapon_B'] = Button(
            image = self.images["equipment_frame"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['weapons_bg'], stats_text, buttons, inventory_items, coords, 'weapons_section', character_armor), 
            relief = "flat")
        buttons['weapon_B'].place(x = 268, y = 87)

        buttons['artifact_B'] = Button(
            image = self.images["equipment_frame"],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['artifacts_bg'], stats_text, buttons, inventory_items, coords, 'artifacts_section', character_armor), 
            relief = "flat")
        buttons['artifact_B'].place(x = 417, y = 87)

        buttons['helmets_section'] = Button(
            image = self.images['helmets_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'helmets_section', background, canvas, self.images['helmets_bg'], character_armor),
            relief = "flat")

        buttons['boots_section'] = Button(
            image = self.images['boots_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'boots_section', background, canvas, self.images['boots_bg'], character_armor),
            relief = "flat")

        buttons['pants_section'] = Button(
            image = self.images['pants_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'pants_section', background, canvas, self.images['pants_bg'], character_armor),
            relief = "flat")

        buttons['chestplates_section'] = Button(
            image = self.images['chestplates_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'chestplates_section', background, canvas, self.images['chestplates_bg'], character_armor),
            relief = "flat")

        buttons['weapons_section'] = Button(
            image = self.images['weapons_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'weapons_section', background, canvas, self.images['weapons_bg'], character_armor),
            relief = "flat")

        buttons['artifacts_section'] = Button(
            image = self.images['artifacts_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'artifacts_section', background, canvas, self.images['artifacts_bg'], character_armor),
            relief = "flat")

        buttons['equip_B'] = Button(
            image = self.images['equip_B'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.btn(),
            relief = "flat")

        buttons['unequip_B'] = Button(
            image = self.images['unequip_B'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.btn(),
            relief = "flat")

        buttons['info_B'] = Button(
            image = self.images['info_B'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.btn(),
            relief = "flat")

        buttons['back_B'] = Button(
            image = self.images['back_B'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_character_sheet(root, background, canvas, self.images['character_bg'], buttons, stats_text, inventory_items, db.data, character_armor),
            relief = "flat")