/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

if instance_exists(obj_arma) and !obj_arma.arma = 0
{
	x = obj_arma.arma_x;
	y = obj_arma.arma_y;
	image_angle = obj_arma.arma_dir;
}else{
	obj_arma.pode_atirar = true;
	instance_destroy();
}








