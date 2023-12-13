'''
This is Part 1 of Sprint 10 Module 1 Project
'''

SELECT_ALL = "SELECT character_id, name FROM charactercreator_character;"

TOTAL_CHARACTERS = "SELECT DISTINCT COUNT(*) FROM charactercreator_character;"

TOTAL_SUBCLASS = "SELECT COUNT(*) FROM charactercreator_necromancer"

TOTAL_ITEMS = "SELECT DISTINCT COUNT(*) FROM armory_item;"

WEAPONS = "SELECT DISTINCT COUNT(*) FROM armory_weapon;"

NON__WEAPONS = '''
SELECT COUNT (*)
FROM armory_item as ai
LEFT JOIN armory_weapon as aw
ON ai.item_id = aw.item_ptr_id
WHERE aw.power IS NULL '''

CHARACTER_ITEMS = '''
SELECT name, COUNT(item_id)
FROM charactercreator_character as cc_char
INNER JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id
'''

CHARACTER_WEAPONS = '''
SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
FROM armory_item AS ai
INNER JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
INNER JOIN charactercreator_character_inventory AS cc_inv
ON ai.item_id = cc_inv.item_id
INNER JOIN charactercreator_character AS cc_char
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id
'''

AVG_CHARACTER_ITEMS = '''
SELECT AVG(total_items) AS average_items_per_char
FROM (SELECT name, COUNT(item_id) AS total_items
FROM charactercreator_character AS cc_char
INNER JOIN charactercreator_character_inventory as cc_inv
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id)
'''

AVG_CHARACTER_WEAPONS = '''
SELECT AVG(total_weapons) AS average_weapons
FROM (SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
FROM armory_item AS ai
INNER JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
INNER JOIN charactercreator_character_inventory AS cc_inv
ON ai.item_id = cc_inv.item_id
INNER JOIN charactercreator_character AS cc_char
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id)
'''
QUERY_LIST = [TOTAL_CHARACTERS,
              TOTAL_SUBCLASS,
              SELECT_ALL,
              TOTAL_ITEMS,
              WEAPONS,
              NON__WEAPONS,
              CHARACTER_ITEMS,
              CHARACTER_WEAPONS,
              AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]
