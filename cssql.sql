-- Connect to the cs_weapon.db SQLite database
ATTACH DATABASE 'cs_weapon.db' AS cs_weapon;
-- Rename the column wepon_id to weapon_id in the cs_weapon.db database
ALTER TABLE {CS_Skins} RENAME COLUMN {wepon_id} TO {weapon_id}
ALTER TABLE {catigory_wepons} RENAME COLUMN {wepon_name} TO {weapon_name}