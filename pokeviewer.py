import requests
from tkinter import ttk
from tkinter import *
from poke_api import get_pokemon_info
from tkinter import messagebox

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

# Create window
root = Tk()
root.title('PokéViewer')
root.resizable(False, False)

# Additional window configuration

# Add frames to the window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(10))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(10), pady=(10))

frm_btm_right = ttk.LabelFrame(root, text ='Stats')
frm_btm_right.grid(row=1, column=1, padx=(10), pady=(10))

# Add widgets to top frame
lbl_name = ttk.Label(frm_top, text='Pokémon Name :')
lbl_name.grid(row=0, column=0, padx=(10), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(10), pady=(10))

def handle_get_info():

    # Get entered pokemon name
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        return

    # Get the info from the API
    poke_info = get_pokemon_info(poke_name)
    if poke_name is None:
        err_msg = f'Unable to tech information for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title='Error', message=err_msg, icon='error') 
    # Populate Info
    lbl_height_value['text'] = f"{poke_info['height']} dm"
    lbl_weight_value['text'] = f"{poke_info['weight']} lbs"
 
    types_list = [t['type']['name'] for t in poke_info['types']]
  

    # Populate Stats
    bar_HP['value'] = poke_info['stats'][0]['base_stat']
    bar_ATK['value'] = poke_info['stats'][1]['base_stat']
    bar_DEF['value'] = poke_info['stats'][2]['base_stat']
    bar_SATK['value'] = poke_info['stats'][3]['base_stat']
    bar_SDEF['value'] = poke_info['stats'][4]['base_stat']
    bar_SPD['value'] = poke_info['stats'][5]['base_stat']

    return

btn_getinfo = ttk.Button(frm_top, text='Find', command=handle_get_info)
btn_getinfo.grid(row=0, column=2, padx=(10), pady=(10))
btn_getinfo = ttk.Label(frm_top)


# Populate widgets in the INFO frame
lbl_height = ttk.Label(frm_btm_left, text='Height :')
lbl_height.grid(row=0, column=0)
lbl_height_value = ttk.Label(frm_btm_left)
lbl_height_value.grid(row=0, column=1)

lbl_weight = ttk.Label(frm_btm_left, text='Weight :')
lbl_weight.grid(row=1, column=0)
lbl_weight_value = ttk.Label(frm_btm_left)
lbl_weight_value.grid(row=1, column=1)

lbl_type = ttk.Label(frm_btm_left, text='Type :')
lbl_type.grid(row=2, column=0)
lbl_type_value = ttk.Label(frm_btm_left)
lbl_type_value.grid(row=2, column=1)


# TODO: Add weight and type

# Populate widgets in the STATS frame
lbl_HP = ttk.Label(frm_btm_right, text='HP:')
lbl_HP.grid(row=0, column=0)
bar_HP = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_HP.grid(row=0, column=1)

lbl_ATK = ttk.Label(frm_btm_right, text='ATTACK:')
lbl_ATK.grid(row=1, column=0)
bar_ATK = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_ATK.grid(row=1, column=1)

lbl_DEF = ttk.Label(frm_btm_right, text='DEFENSE:')
lbl_DEF.grid(row=2, column=0)
bar_DEF = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_DEF.grid(row=2, column=1)

lbl_SATK = ttk.Label(frm_btm_right, text='SPECIAL ATTACK:')
lbl_SATK.grid(row=3, column=0)
bar_SATK = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_SATK.grid(row=3, column=1)

lbl_SDEF = ttk.Label(frm_btm_right, text='SPECIAL DEFENSE:')
lbl_SDEF.grid(row=4, column=0)
bar_SDEF = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_SDEF.grid(row=4, column=1)

lbl_SPD = ttk.Label(frm_btm_right, text='SPEED')
lbl_SPD.grid(row=5, column=0)
bar_SPD = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_SPD.grid(row=5, column=1)

# Loop until window is closed
root.mainloop()
