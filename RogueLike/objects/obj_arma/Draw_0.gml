/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

if sprite != -1
{
	if !melee
	{
		var recoil_x = lengthdir_x(recoil, arma_dir);
		var recoil_y = lengthdir_y(recoil, arma_dir);
		draw_sprite_ext(sprite, image_index, arma_x - recoil_x, arma_y - recoil_y, xscale, 1, arma_dir, c_white, 1);
	}else{
		if !instance_exists(obj_hit)
		{
			draw_sprite_ext(sprite, image_index, arma_x, arma_y, 1, xscale, arma_dir, c_white, 1);
		}
	}
}







