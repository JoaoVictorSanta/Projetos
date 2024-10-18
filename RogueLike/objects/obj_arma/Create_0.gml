//slots das armas
slot[0] = 0;
slot[1] = 0;

//Sem arma
armas[0] = ds_map_create();
ds_map_add(armas[0], "melee", false);
ds_map_add(armas[0], "sprite", -1);
ds_map_add(armas[0], "proj", -1);
ds_map_add(armas[0], "proj_count", -1);
ds_map_add(armas[0], "proj_spd", 0);
ds_map_add(armas[0], "proj_damage", 0);
ds_map_add(armas[0], "proj_delay", 0);
ds_map_add(armas[0], "automatic", false);
ds_map_add(armas[0], "drop", false);
ds_map_add(armas[0], "ammo", -1);
ds_map_add(armas[0], "ammo_size", -1);
ds_map_add(armas[0], "carregamento", -1);
ds_map_add(armas[0], "stealth", true);

//Pistola
armas[1] = ds_map_create();
ds_map_add(armas[1], "melee", false);
ds_map_add(armas[1], "sprite", spr_pistola);
ds_map_add(armas[1], "proj", spr_proj);
ds_map_add(armas[1], "proj_count", 1);
ds_map_add(armas[1], "proj_spd", 8);
ds_map_add(armas[1], "proj_damage", 15);
ds_map_add(armas[1], "proj_delay", 12);
ds_map_add(armas[1], "automatic", true);
ds_map_add(armas[1], "drop", obj_pistola);
ds_map_add(armas[1], "ammo", 10);
ds_map_add(armas[1], "ammo_size", 10);
ds_map_add(armas[1], "carregamento", 60);
ds_map_add(armas[1], "stealth", false);

//Shotgun
armas[2] = ds_map_create();
ds_map_add(armas[2], "melee", false);
ds_map_add(armas[2], "sprite", spr_shotgun);
ds_map_add(armas[2], "proj", spr_proj);
ds_map_add(armas[2], "proj_count", 3);
ds_map_add(armas[2], "proj_spd", 10);
ds_map_add(armas[2], "proj_damage", 30);
ds_map_add(armas[2], "proj_delay", 60);
ds_map_add(armas[2], "automatic", true);
ds_map_add(armas[2], "drop", obj_shotgun);
ds_map_add(armas[2], "ammo", 3);
ds_map_add(armas[2], "ammo_size", 3);
ds_map_add(armas[2], "carregamento", 60);
ds_map_add(armas[2], "stealth", false);

//bastao
armas[3] = ds_map_create();
ds_map_add(armas[3], "melee", true);
ds_map_add(armas[3], "sprite", spr_arma_branca);
ds_map_add(armas[3], "proj", spr_arma_branca_batendo);
ds_map_add(armas[3], "proj_count", 1);
ds_map_add(armas[3], "proj_spd", 5);
ds_map_add(armas[3], "proj_damage", 35);
ds_map_add(armas[3], "proj_delay", 50);
ds_map_add(armas[3], "automatic", true);
ds_map_add(armas[3], "drop", obj_bastao);
ds_map_add(armas[3], "ammo", 200);
ds_map_add(armas[3], "ammo_size", 200);
ds_map_add(armas[3], "carregamento", -1);
ds_map_add(armas[3], "stealth", true);

arma_id = -1;
arma_dir = -1;
arma_x = -1;
arma_y = -1;
pode_atirar = true;
animacao = false;

slot_selecionado = 0;

scr_mudar_arma(self, slot[0]);

ammo_atual_0 = armas[slot[0]][? "ammo_size"];
ammo_atual_1 = armas[slot[1]][? "ammo_size"];
ammo_total = 100;
ammo_atual = -1;
durabilidade = 10;
recoil = 0;


