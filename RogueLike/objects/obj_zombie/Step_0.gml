/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

switch estado
{
	case "parado":
		var range = 300;
		var linha = collision_line(x, y, obj_player.x, obj_player.y , obj_bloco, 0, 0);
		path_end();
		if distance_to_object(obj_player) <= range and !linha
		{
			estado = "seguindo_player";
			timer = room_speed * 5;
		}
	break;

	case "seguindo_player":
		var range = 300;
		var linha = collision_line(x, y, obj_player.x, obj_player.y , obj_bloco, 0, 0);
		var x1 = x;
		var y1 = y;
		var x2 = (obj_player.x div 64) * 64 + 32;
		var y2 = (obj_player.y div 64) * 64 + 32;

		if mp_grid_path(obj_mapa.mp_grid, caminho, x1, y1, x2, y2, true)
		{
			path_start(caminho, velc, path_action_stop, false);
		}
		
		if (distance_to_object(obj_player) > range or linha) and timer > 0 and !infestacao
		{
			timer --;
		}
		
		if (distance_to_object(obj_player) > range or linha) and timer <= 0 and !infestacao
		{
			estado = "parado";
		}
	break;
}

hit_alpha = lerp(hit_alpha, 0, 0.1);

if vida <= 0 
{
	
	instance_destroy();
	obj_controle.objetivo = true;
	obj_controle.n_zombies--;
}






