/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor
var tecla_direita = keyboard_check(ord("D"));
var tecla_esquerda = keyboard_check(ord("A"));
var tecla_cima = keyboard_check(ord("W"));
var tecla_baixo = keyboard_check(ord("S"));

var teclas = tecla_direita - tecla_esquerda != 0 || tecla_baixo - tecla_cima != 0;

move_dir = point_direction(0,0,tecla_direita - tecla_esquerda, tecla_baixo - tecla_cima);

hveloc = lengthdir_x(veloc * teclas, move_dir);
vveloc = lengthdir_y(veloc * teclas, move_dir);

if place_meeting(x + hveloc, y, obj_bloco)
{
	while !place_meeting(x + sign(hveloc), y, obj_bloco)
	{
		x += sign(hveloc);
	}
	hveloc = 0;
}
if place_meeting(x, y + vveloc, obj_bloco)
{
	while !place_meeting(x, y + sign(vveloc), obj_bloco)
	{
		y += sign(vveloc);
	}
	vveloc = 0;
}

x += hveloc;
y += vveloc;

with(arma_equip)
{
	
	var mb;
	var tecla_drop = keyboard_check_pressed(ord("F"));
	var tecla_slot = keyboard_check_pressed(ord("Q"));
	var tecla_reload = keyboard_check_pressed(ord("R"));
	var tecla_pegar = keyboard_check_pressed(ord("E"));
	
	if automatic
	{
		mb = mouse_check_button(mb_left);
	}else{
		mb = mouse_check_button_pressed(mb_left);
	}
	
	arma_dir = point_direction(x, y, mouse_x, mouse_y);
	if mb
	{
		if melee = true
		{
			bater();
		}else{
			atirar();
		}
	}
	
	if tecla_drop and arma > 0
	{
		arma_drop();
	}else if tecla_drop and arma == 0{
		pegar_arma();
	}
	
	if tecla_slot{
		trocar_arma();
	}
	
	if tecla_reload
	{
		reload();
	}
}

hit_alpha = lerp(hit_alpha, 0, 0.01);