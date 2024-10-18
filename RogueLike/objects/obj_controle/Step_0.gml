/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

if instance_exists(obj_player)
{
	if obj_player.vida <= 0
	{
		room_restart();
	}
}

function infestacao()
{
	if !instance_exists(obj_infestacao)
	{
		instance_create_layer(x,y,"Instances", obj_infestacao);
	}
}

if !objetivo
{
	if instance_exists(obj_hall)
	{
		instance_deactivate_object(obj_hall);
	}
}else{
	instance_activate_object(obj_hall);
}






