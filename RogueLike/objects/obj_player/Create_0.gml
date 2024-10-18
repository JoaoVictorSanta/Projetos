/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

vida = 4;

hveloc = -1;
vveloc = -1;
veloc = 4;

pode_tomar_dano = 1;

depth = -1;

arma_equip = instance_create_layer(x,y,"Armas",obj_arma);
arma_equip.arma_id = self;

hit_alpha = 0;
hit_color = c_red;
