from tkinter import HIDDEN, Button, Canvas, Label, PhotoImage, DISABLED
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

    "h":                     PhotoImage(file = f"images\items\\empty.png"),
    "h_F":                   PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    "c":                     PhotoImage(file = f"images\items\\empty.png"),
    "c_F":                   PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    "p":                     PhotoImage(file = f"images\items\\empty.png"),
    "p_F":                   PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    "b":                     PhotoImage(file = f"images\items\\empty.png"),
    "b_F":                   PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    "w":                     PhotoImage(file = f"images\items\\empty.png"),
    "w_F":                   PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    "a":                     PhotoImage(file = f"images\items\\empty.png"),
    "a_F":                   PhotoImage(file = f"images\character_sheet\equipment_frame.png"),
    # minecraft
    "DBM":                  PhotoImage(file = f"images\items\\DBM.png"),
    "DBM_F":                PhotoImage(file = f"images\items\\DBM_F.png"),
    "DCM":                  PhotoImage(file = f"images\items\\DCM.png"),
    "DCM_F":                PhotoImage(file = f"images\items\\DCM_F.png"),
    "DHM":                  PhotoImage(file = f"images\items\\DHM.png"),
    "DHM_F":                PhotoImage(file = f"images\items\\DHM_F.png"),
    "DPM":                  PhotoImage(file = f"images\items\\DPM.png"),
    "DPM_F":                PhotoImage(file = f"images\items\\DPM_F.png"),
    "DSM":                  PhotoImage(file = f"images\items\\DSM.png"),
    "DSM_F":                PhotoImage(file = f"images\items\\DSM_F.png"),
    "TOUM":                 PhotoImage(file = f"images\items\\TOUM.png"),
    "TOUM_F":               PhotoImage(file = f"images\items\\TOUM_F.png"),
    # monster hunter
    "APMMu_F":              PhotoImage(file = f"images\items\\APMMu_F.png"),
    "APMMu":                PhotoImage(file = f"images\items\\APMMu.png"),
    "FBMu_F":               PhotoImage(file = f"images\items\\FBMu_F.png"),
    "FBMu":                 PhotoImage(file = f"images\items\\FBMu.png"),
    # final fantasy
    "BSF_F":                PhotoImage(file = f"images\items\\BSF_F.png"),
    "BSF":                  PhotoImage(file = f"images\items\\BSF.png"),
    # star wars
    "LSS_F":                PhotoImage(file = f"images\items\\LSS_F.png"),
    "LSS":                  PhotoImage(file = f"images\items\\LSS.png"),
    "DBBS_F":               PhotoImage(file = f"images\items\\DBBS_F.png"),
    "DBBS":                 PhotoImage(file = f"images\items\\DBBS.png"),
    "DBCS_F":               PhotoImage(file = f"images\items\\DBCS_F.png"),
    "DBCS":                 PhotoImage(file = f"images\items\\DBCS.png"),
    "DBHS_F":               PhotoImage(file = f"images\items\\DBHS_F.png"),
    "DBHS":                 PhotoImage(file = f"images\items\\DBHS.png"),
    "DBPS_F":               PhotoImage(file = f"images\items\\DBPS_F.png"),
    "DBPS":               PhotoImage(file = f"images\items\\DBPS.png"),
    # destiny
    "SCD_F":                PhotoImage(file = f"images\items\\SCD_F.png"),
    "SCD":                  PhotoImage(file = f"images\items\\SCD.png"),
    # doom
    "BFGD_F":               PhotoImage(file = f"images\items\\BFGD_F.png"),
    "BFGD":                 PhotoImage(file = f"images\items\\BFGD.png"),
    "DBD_F":                PhotoImage(file = f"images\items\\DBD_F.png"),
    "DBD":                  PhotoImage(file = f"images\items\\DBD.png"),
    "DCD_F":                PhotoImage(file = f"images\items\DCD_F.png"),
    "DCD":                  PhotoImage(file = f"images\items\DCD.png"),
    "DHD_F":                PhotoImage(file = f"images\items\DHD_F.png"),
    "DHD":                  PhotoImage(file = f"images\items\DHD.png"),
    "DPD_F":                PhotoImage(file = f"images\items\DPD_F.png"),
    "DPD":                  PhotoImage(file = f"images\items\DPD.png"),
    # halo
    "ESH_F":                PhotoImage(file = f"images\items\\ESH_F.png"),
    "ESH":                  PhotoImage(file = f"images\items\\ESH.png"),
    "HBH_F":                PhotoImage(file = f"images\items\\HBH_F.png"),
    "HBH":                  PhotoImage(file = f"images\items\\HBH.png"),
    "HCH_F":                PhotoImage(file = f"images\items\\HCH_F.png"),
    "HCH":                  PhotoImage(file = f"images\items\\HCH.png"),
    "HHH_F":                PhotoImage(file = f"images\items\\HHH_F.png"),
    "HCH":                  PhotoImage(file = f"images\items\\HCH.png"),
    "HPH_F":                PhotoImage(file = f"images\items\\HPH_F.png"),
    "HPH":                  PhotoImage(file = f"images\items\\HPH.png"),
    # marvel
    "MTMa_F":               PhotoImage(file = f"images\items\\MTMa_F.png"),
    "MTMa":                 PhotoImage(file = f"images\items\\MTMa.png"),
    "IMBMa_F":              PhotoImage(file = f"images\items\\IMBMa_F.png"),
    "IMBMa":                PhotoImage(file = f"images\items\\IMBMa.png"),
    "IMCMa_F":              PhotoImage(file = f"images\items\\IMCMa_F.png"),
    "IMCMa":                PhotoImage(file = f"images\items\\IMCMa.png"),
    "IMHMa_F":              PhotoImage(file = f"images\items\\IMHMa_F.png"),
    "IMHMa":                PhotoImage(file = f"images\items\\IMHMa.png"),
    "IMPMa_F":              PhotoImage(file = f"images\items\\IMPMa_F.png"),
    "IMPMa":                PhotoImage(file = f"images\items\\IMPMa.png"),
    # megaman
    "MBMe_F":               PhotoImage(file = f"images\items\\MBMe_F.png"),
    "MBMe":                 PhotoImage(file = f"images\items\\MBMe.png"),
    "MCMe_F":               PhotoImage(file = f"images\items\\MCMe_F.png"),
    "MCMe":                 PhotoImage(file = f"images\items\\MCMe.png"),
    "MHMe_F":               PhotoImage(file = f"images\items\\MHMe_F.png"),
    "MHMe":                 PhotoImage(file = f"images\items\\MHMe.png"),
    "MPMe_F":               PhotoImage(file = f"images\items\\MPMe_F.png"),
    "MPMe":                 PhotoImage(file = f"images\items\\MPMe.png"),
    # genshin
    "SBG_F":                PhotoImage(file = f"images\items\\SBG_F.png"),
    "SBG":                  PhotoImage(file = f"images\items\\SBG.png")
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
        # canvas.wm_attributes("-transparentcolor", 'white')

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
        item_stats = {
            'atk': canvas.create_text(
                215.0, 584.5,
                text = "100",
                fill = "#000000",
                state = HIDDEN,
                font = ("Minecraft", int(36.0))),
            'def': canvas.create_text(
                215.0, 629.5,
                text = "100",
                fill = "#000000",
                state = HIDDEN,
                font = ("Minecraft", int(36.0))),
            'vel': canvas.create_text(
                428.0, 584.5,
                text = "100",
                fill = "#000000",
                state = HIDDEN,
                font = ("Minecraft", int(36.0))),
            'mag': canvas.create_text(
                428.0, 629.5,
                text = "100",
                fill = "#000000",
                state = HIDDEN,
                font = ("Minecraft", int(36.0)))
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
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'helmets_section', code, db, item_stats, canvas))
        for item in db.chestplates:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'chestplates_section', code, db, item_stats, canvas))
        for item in db.pants:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'pants_section', code, db, item_stats, canvas))
        for item in db.boots:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'boots_section', code, db, item_stats, canvas))
        for item in db.weapons:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'weapons_section', code, db, item_stats, canvas))
        for item in db.artifacts:
            new_button = Button(
                image = self.images[item['code']],
                command = lambda: functions.select_item(),
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")
            inventory_items[item['code']] = new_button
            inventory_items[item['code']].configure(command = lambda code = item['code']: functions.select_item(inventory_items[code], character_armor, 'artifacts_section', code, db, item_stats, canvas))

        # Equipment of the character
        character_armor = {'helmets_section':       [inventory_items[db.character['armor']['helmet']], db.character['armor']['helmet'],
                                                    Label(image = self.images[db.character['armor']['helmet']])], 
                            'chestplates_section':  [inventory_items[db.character['armor']['chestplate']], db.character['armor']['chestplate'],
                                                    Label(image = self.images[db.character['armor']['chestplate']])], 
                            'pants_section':        [inventory_items[db.character['armor']['pants']], db.character['armor']['pants'],
                                                    Label(image = self.images[db.character['armor']['pants']])], 
                            'boots_section':        [inventory_items[db.character['armor']['boots']], db.character['armor']['boots'],
                                                    Label(image = self.images[db.character['armor']['boots']])], 
                            'weapons_section':      [inventory_items[db.character['weapon']], db.character['weapon'],
                                                    Label(image = self.images[db.character['weapon']])], 
                            'artifacts_section':    [inventory_items[db.character['artifact']], db.character['artifact'],
                                                    Label(image = self.images[db.character['artifact']])]}
        for item in character_armor:
            character_armor[item][0]['state'] = DISABLED

        buttons = {}

        buttons['helmet_B'] = Button(
            image = self.images[character_armor['helmets_section'][1]+'_F'],
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['helmets_bg'], stats_text, buttons, inventory_items, coords, 'helmets_section', character_armor, item_stats),
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")
        buttons['helmet_B'].place(x = 162, y = 226)
        # character_armor['helmets_section'][2].place(x= 217, y = 281, anchor = "center")

        buttons['chestplate_B'] = Button(
            image = self.images[character_armor['chestplates_section'][1]+'_F'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['chestplates_bg'], stats_text, buttons, inventory_items, coords, 'chestplates_section', character_armor, item_stats),
            relief = "flat")
        buttons['chestplate_B'].place(x = 523, y = 224)
        # character_armor['chestplates_section'][2].place(x= 579, y = 281, anchor = "center")
        
        buttons['pants_B'] = Button(
            image = self.images[character_armor['pants_section'][1]+'_F'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['pants_bg'], stats_text, buttons, inventory_items, coords, 'pants_section', character_armor, item_stats),
            relief = "flat")
        buttons['pants_B'].place(x = 162, y = 355)
        # character_armor['pants_section'][2].place(x= 217, y = 412, anchor = "center")
        
        buttons['boots_B'] = Button(
            image = self.images[character_armor['boots_section'][1]+'_F'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['boots_bg'], stats_text, buttons, inventory_items, coords, 'boots_section', character_armor, item_stats),
            relief = "flat")
        buttons['boots_B'].place(x = 523, y = 355)
        # character_armor['boots_section'][2].place(x= 579, y = 412, anchor = "center")
        
        buttons['weapon_B'] = Button(
            image = self.images[character_armor['weapons_section'][1]+'_F'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['weapons_bg'], stats_text, buttons, inventory_items, coords, 'weapons_section', character_armor, item_stats), 
            relief = "flat")
        buttons['weapon_B'].place(x = 268, y = 87)
        # character_armor['weapons_section'][2].place(x= 324, y = 144, anchor = "center")

        buttons['artifact_B'] = Button(
            image = self.images[character_armor['artifacts_section'][1]+'_F'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_inventory_sheet(root, db, background, canvas, self.images['artifacts_bg'], stats_text, buttons, inventory_items, coords, 'artifacts_section', character_armor, item_stats), 
            relief = "flat")
        buttons['artifact_B'].place(x = 417, y = 87)
        # character_armor['artifacts_section'][2].place(x= 473, y = 144, anchor = "center")

        buttons['helmets_section'] = Button(
            image = self.images['helmets_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'helmets_section', background, canvas, self.images['helmets_bg'], character_armor, item_stats),
            relief = "flat")

        buttons['boots_section'] = Button(
            image = self.images['boots_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'boots_section', background, canvas, self.images['boots_bg'], character_armor, item_stats),
            relief = "flat")

        buttons['pants_section'] = Button(
            image = self.images['pants_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'pants_section', background, canvas, self.images['pants_bg'], character_armor, item_stats),
            relief = "flat")

        buttons['chestplates_section'] = Button(
            image = self.images['chestplates_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'chestplates_section', background, canvas, self.images['chestplates_bg'], character_armor, item_stats),
            relief = "flat")

        buttons['weapons_section'] = Button(
            image = self.images['weapons_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'weapons_section', background, canvas, self.images['weapons_bg'], character_armor, item_stats),
            relief = "flat")

        buttons['artifacts_section'] = Button(
            image = self.images['artifacts_section'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.inventory_sheet_button(buttons, db, coords, inventory_items, 'artifacts_section', background, canvas, self.images['artifacts_bg'], character_armor, item_stats),
            relief = "flat")

        # buttons['equip_B'] = Button(
        #     image = self.images['equip_B'],
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     command = lambda: functions.btn(),
        #     relief = "flat")

        # buttons['unequip_B'] = Button(
        #     image = self.images['unequip_B'],
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     command = lambda: functions.btn(),
        #     relief = "flat")

        # buttons['info_B'] = Button(
        #     image = self.images['info_B'],
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     command = lambda: functions.btn(),
        #     relief = "flat")

        buttons['back_B'] = Button(
            image = self.images['back_B'],
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: functions.initialize_character_sheet(root, background, canvas, self.images['character_bg'], buttons, stats_text, inventory_items, db.data, character_armor, self.images, item_stats),
            relief = "flat")