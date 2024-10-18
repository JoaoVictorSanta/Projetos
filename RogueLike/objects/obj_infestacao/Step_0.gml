/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

relogio = string(minutos) + " : " + string(segundos);

if contador > 0
{
	contador--;
}else{
	contador = room_speed;
	segundos--;
	tempo--;
}

if segundos < 0
{
	segundos = 59;
	minutos--;
}

if !tempo > 0 and instance_exists(obj_mapa)
{
	segundos = 0;
	minutos = 0;
	infest();
}






