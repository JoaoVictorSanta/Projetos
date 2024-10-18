/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor


max_infest = 60;
tempo = 3 * 60;
minutos = floor(tempo / 60);
segundos = tempo - 60 * minutos;

relogio = -1;

contador = room_speed;

function infest()
{

	if max_infest > 0
	{
		var inst = instance_create_layer(obj_hall.x + irandom_range(-32, 32), obj_hall.y + irandom_range(-32, 32), "Instances", obj_zombie);
		inst.estado = "seguindo_player";
		inst.infestacao = true;
		max_infest --;
	}
}

