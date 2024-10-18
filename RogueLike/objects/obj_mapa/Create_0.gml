/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

instance_create_layer(x,y,"Instances",obj_controle)

cell_size = 64;

grid_width = room_width div cell_size;
grid_height = room_height div cell_size;

grid = ds_grid_create(grid_width, grid_height);
mp_grid = mp_grid_create(0, 0, grid_width, grid_height, cell_size, cell_size);

ds_grid_clear(grid, 0);

randomize();

var xx = grid_width div 2;
var yy = grid_height div 2;

var lado = irandom(3);

parede = 0;
rua = 1;
corredor = 2;

hortifrute = 3;

acougue = 4;
padaria = 5;
entrada = 6;

estoque = 7;

porta = 8;
var max_hort = 5;
var max_acou = 12;
var max_pada = 12;
var max_est = 3;
var max_corr = 15;

coord = ds_list_create();
ds_list_add(coord, 0);
ds_list_add(coord, 1);
ds_list_add(coord, 2);
ds_list_add(coord, 3);

locais = ds_list_create();
ds_list_add(locais, parede);
ds_list_add(locais, acougue);
ds_list_add(locais, padaria);
ds_list_add(locais, entrada);

var porcent = irandom(100);
var qtd_estoque;

if porcent < 2
{
	qtd_estoque = 4;
}else if porcent < 5
{
	qtd_estoque = 3;
}else if porcent < 20
{
	qtd_estoque = 2;
}else{
	qtd_estoque = 1;
}

ds_grid_set_region(grid, 0, 0, grid_width, grid_height, parede);

ds_grid_set_region(grid, xx - 17, yy - 17, xx + 17, yy + 17, rua);

for (i = 0; i < 4; i++)
{
	var angulo = i * 90 ;
	var sinal_x = sign(lengthdir_x(1, angulo + 45));
	var sinal_y = sign(lengthdir_y(1, angulo + 45));
	
	if i == lado
	{
		ds_grid_set_region(grid, xx + 2 * sinal_x, yy + 2 * sinal_y, xx + 14 * sinal_x, yy + 14 * sinal_y, hortifrute);
	}else{
		ds_grid_set_region(grid, xx + 2 * sinal_x, yy + 2 * sinal_y, xx + 14 * sinal_x, yy + 14 * sinal_y, corredor);
		for(j = 0; j < 4; j++)
		{
			ds_grid_set_region(grid, xx + 2 * sinal_x, yy + (2 + j * 4) * sinal_y, xx + 14 * sinal_x, yy + (2 + j * 4) * sinal_y, parede);
		}
	}
	
	var pos = irandom(ds_list_size(locais) - 1);
	
	var dis_ponto_x = lengthdir_x(19, angulo);
	var larg_rec_x = lengthdir_x(17, angulo + 90);
	var comp_rec_x = lengthdir_x(6, angulo);
	var dis_ponto_y = lengthdir_y(19, angulo);
	var larg_rec_y = lengthdir_y(17, angulo + 90);
	var comp_rec_y = lengthdir_y(6, angulo);
	
	ds_grid_set_region(grid, xx + dis_ponto_x + larg_rec_x, yy + dis_ponto_y + larg_rec_y, xx + dis_ponto_x - larg_rec_x+ comp_rec_x, yy + dis_ponto_y - larg_rec_y + comp_rec_y, locais[| pos]);
	
	ds_list_delete(locais, pos);
	
	if grid[# xx + lengthdir_x(19, angulo), yy + lengthdir_y(19, angulo)] != 0
	{
		ds_grid_set_region(grid, xx + lengthdir_x(18, angulo) + lengthdir_x(1, angulo + 90), yy + lengthdir_y(18, angulo) + lengthdir_y(1, angulo + 90), xx + lengthdir_x(18, angulo) - lengthdir_x(1, angulo + 90), yy + lengthdir_y(18, angulo) - lengthdir_y(1, angulo + 90), porta);
	}

}


for(var i = 0; i < qtd_estoque; i ++)
{

	var pos = irandom(ds_list_size(coord) - 1);
	var angulo = coord[| pos] * 90;
	var sinal_x = sign(lengthdir_x(1, angulo + 45));
	var sinal_y = sign(lengthdir_y(1, angulo + 45));
	ds_grid_set_region(grid, xx + 19 * sinal_x, yy + 19 * sinal_y, xx + 25 * sinal_x, yy + 25 * sinal_y, estoque);	
	if grid[# xx + 15 * sinal_x, yy + 22 * sinal_y] != parede and grid[# xx + 15 * sinal_x, yy + 22 * sinal_y] != entrada
	{
		ds_grid_set_region(grid, xx + 18 * sinal_x, yy + 22 * sinal_y, xx + 18 * sinal_x, yy + 22 * sinal_y, porta);	
	}
	if grid[# xx + 22 * sinal_x, yy + 15 * sinal_y] != parede and grid[# xx + 22 * sinal_x, yy + 15 * sinal_y] != entrada
	{
		ds_grid_set_region(grid, xx + 22 * sinal_x, yy + 18 * sinal_y, xx + 22 * sinal_x, yy + 18 * sinal_y, porta);
	}
	ds_list_delete(coord, pos);
}

for (var i = 0; i < grid_width; i++)
{
	for (var j = 0; j < grid_height; j++)
	{
		if (grid[# i, j] == parede)
		{
			instance_create_layer(i * cell_size, j * cell_size, "Instances", obj_bloco);
		}
		if (grid[# i, j] == entrada)
		{
			if !instance_exists(obj_player)
			{
				ang = round(point_direction(xx,yy,i,j) / 90) * 90;
				ang_x = sign(lengthdir_x(1, ang));
				ang_y = sign(lengthdir_y(1, ang));
				instance_create_layer(xx * cell_size + 32 + lengthdir_x(23 * cell_size, ang), yy * cell_size + 32 + lengthdir_y(23 * cell_size, ang), "Instances", obj_player);
				var inst_hall = instance_create_layer(xx * cell_size + 32 + lengthdir_x(24.5 * cell_size, ang), yy * cell_size + 32 + lengthdir_y(24.5 * cell_size, ang), "Instances", obj_hall);
				inst_hall.image_angle = ang + 90;
				instance_create_layer(xx * cell_size + 32 - lengthdir_x(64, ang) + lengthdir_x(64, ang + 90) + lengthdir_x(23 * cell_size, ang), yy * cell_size + 32 - lengthdir_y(64, ang) + lengthdir_y(64, ang + 90) + lengthdir_y(23 * cell_size, ang), "Armas", obj_bastao);
				instance_create_layer(xx * cell_size + 32 - lengthdir_x(64, ang) - lengthdir_x(64, ang + 90) + lengthdir_x(23 * cell_size, ang), yy * cell_size + 32 - lengthdir_y(64, ang) - lengthdir_y(64, ang + 90) + lengthdir_y(23 * cell_size, ang), "Armas", obj_pistola);
				instance_create_layer(xx * cell_size + 32 - lengthdir_x(64, ang) + lengthdir_x(23 * cell_size, ang), yy * cell_size + 32 - lengthdir_y(64, ang) + lengthdir_y(23 * cell_size, ang), "Armas", obj_shotgun);
			}
		}
		if (grid[# i, j] == hortifrute)
		{
			if(max_hort > 0)
			{
				var chances = 25;
				if(irandom(chances)) == chances
				{
					instance_create_layer(i * cell_size + 32, j * cell_size + 32, "Instances", obj_zombie);
					max_hort--;
				}
			}
		}
		if (grid[# i, j] == estoque)
		{
			if(max_est > 0)
			{
				var chances = 25;
				if(irandom(chances)) == chances
				{
					instance_create_layer(i * cell_size + 32, j * cell_size + 32, "Instances", obj_zombie);
					max_est--;
				}
			}
		}
		if (grid[# i, j] == padaria)
		{
			if(max_pada > 0)
			{
				var chances = 25;
				if(irandom(chances)) == chances
				{
					instance_create_layer(i * cell_size + 32, j * cell_size + 32, "Instances", obj_zombie);
					max_pada--;
				}
			}
		}
		if (grid[# i, j] == acougue)
		{
			if(max_acou > 0)
			{
				var chances = 25;
				if(irandom(chances)) == chances
				{
					instance_create_layer(i * cell_size + 32, j * cell_size + 32, "Instances", obj_zombie);
					max_acou--;
				}
			}
		}
		if (grid[# i, j] == corredor)
		{
			if(max_corr > 0)
			{
				var chances = 50;
				if(irandom(chances)) == chances
				{
					instance_create_layer(i * cell_size + 32, j * cell_size + 32, "Instances", obj_zombie);
					max_corr--;
				}
			}
		}		
	}
}

mp_grid_add_instances(grid, obj_bloco, true);

