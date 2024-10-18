/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

if other.melee_damage = false
{
	var dir = point_direction(obj_player.x, obj_player.y, other.x, other.y);
	other.melee_damage = true;
	other.vida -= damage;
	other.hit_alpha = 1;
	other.alarm[0] = 10;
	var xx = other.x;
	var yy = other.y;
	other.x = lerp(other.x, xx + lengthdir_x(15, dir), 1);
	other.y = lerp(other.y, yy + lengthdir_y(15, dir), 1);
	obj_arma.ammo--;
	
}






