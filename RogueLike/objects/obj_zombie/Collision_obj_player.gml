/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor


if other.pode_tomar_dano == 1
{
	other.vida--;
	other.pode_tomar_dano = 0;
	other.alarm[0] = room_speed * 1;
	other.hit_alpha = 1;
	obj_controle.infestacao();
}








