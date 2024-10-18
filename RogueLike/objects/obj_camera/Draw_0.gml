/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor


depth = -100;
var ini_x = camera_get_view_x(view_camera[0]);
var ini_y = camera_get_view_y(view_camera[0]);
var end_x = camera_get_view_width(view_camera[0]);
var end_y = camera_get_view_height(view_camera[0]);
	
var cell_x = floor(obj_player.x / obj_mapa.cell_size);
var cell_y = floor(obj_player.y / obj_mapa.cell_size);
	
switch ds_grid_get(obj_mapa.grid, cell_x, cell_y)
{
	case obj_mapa.entrada:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Entrada");
	break;
	case obj_mapa.corredor:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Corredores");
	break;
	case obj_mapa.rua:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Corredores");
	break;
	case obj_mapa.hortifrute:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Hortifrute");
	break;
	case obj_mapa.padaria:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Padaria");
	break;
	case obj_mapa.acougue:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Acougue");
	break;
	case obj_mapa.estoque:
	draw_text(ini_x + 450, ini_y + 32 / 2, "Estoque");
	break;
}

	draw_text(ini_x + 32, ini_y + 32 / 2, obj_controle.n_zombies);
	draw_text(ini_x + 64, ini_y + 32 / 2, obj_player.vida);
	
	
var sprite_0 = obj_arma.armas[obj_arma.slot[0]][? "sprite"];
var sprite_1 = obj_arma.armas[obj_arma.slot[1]][? "sprite"];
var ammo_0 = obj_arma.armas[obj_arma.slot[0]][? "ammo"];
var ammo_1 = obj_arma.armas[obj_arma.slot[1]][? "ammo"];


draw_text(ini_x + 512, ini_y + 32, obj_arma.ammo_total);

if obj_arma.slot_selecionado = 0
{
	draw_arrow(ini_x + 128, ini_y + 64, ini_x + 128, ini_y + 48, 20);
}else{
	draw_arrow(ini_x + 256, ini_y + 64, ini_x + 256, ini_y + 48, 20);
}
	
if sprite_0 != -1
{
	draw_sprite(sprite_0, 0, ini_x + 128, ini_y + 32);
	if obj_arma.ammo_atual != -1
	{
		draw_text(ini_x + 384, ini_y + 32, obj_arma.ammo_atual);
	}
}
if sprite_1 != -1
{	
	draw_sprite(sprite_1, 0, ini_x + 256, ini_y + 32);
	if obj_arma.ammo_atual != -1
	{
		draw_text(ini_x + 384, ini_y + 32, obj_arma.ammo_atual);
	}
}

if instance_exists(obj_infestacao)
{
	draw_text(ini_x + 576, ini_y + 32, obj_infestacao.relogio);
}