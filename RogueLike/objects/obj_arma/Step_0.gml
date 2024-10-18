/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

if instance_exists(arma_id)
{
	x = arma_id.x;
	y = arma_id.y;
	
	mouse_dir = point_direction(x, y, mouse_x, mouse_y);
	
	xscale = sign(lengthdir_x(1, mouse_dir));
	
	arma_x = x + lengthdir_x(20, arma_dir);
	arma_y = y + lengthdir_y(20, arma_dir);
	
	ammo_atual = ammo;
	
	depth = arma_id.depth -1;
	
	image_angle = arma_dir;
	
	function bater()
	{
		if !arma > 0
		{
			return false;
		}
		
		if !pode_atirar
		{
			return false;
		}
		
		if !ammo > 0
		{
			return false;
		}		
		
		if alarm[1] > 0
		{
			return false;
		}
		
		for (var i = 0; i < proj_count; i ++)
		{
			var proj_inst = instance_create_layer(arma_x, arma_y, "Projeteis", obj_hit);
			proj_inst.sprite_index = proj;
			proj_inst.damage = proj_damage;
			proj_inst.image_angle = arma_dir;
			proj_inst.image_speed = proj_spd;
			proj_inst.image_yscale = xscale;
		}
		
		if !stealth
		{
			obj_controle.infestacao();
		}

		alarm[0] = proj_delay;
		pode_atirar = false;
		
	}
	
	function atirar()
	{
		
		if !arma > 0
		{
			return false;
		}
		
		if !pode_atirar
		{
			return false;
		}
		
		if !ammo > 0
		{
			return false
		}		
		
		if alarm[1] > 0
		{
			return false;
		}

		for (var i = 0; i < proj_count; i ++)
		{
			if ammo < 1
			{
				return false;
			}
			
			var proj_inst = instance_create_layer(arma_x, arma_y, "Projeteis", obj_proj);
			proj_inst.sprite_index = proj;
			var dist = 6;
			var dir = arma_dir + (dist * i);
			proj_inst.direction = dir;
			proj_inst.image_angle = dir;
			proj_inst.speed = proj_spd;
			proj_inst.damage = proj_damage;
			ammo--;
		}
	
		recoil = 8;
		pode_atirar = false;
		alarm[0] = proj_delay;
		
		if !stealth
		{
			obj_controle.infestacao();
		}
	}
	
	function arma_drop()
	{
		
		if alarm[1] > 0
		{
			return false;
		}
		
		if !drop > 0
		{
			return false;
		}
		
		var inst = instance_create_layer(arma_x, arma_y, "Instances", drop);
		inst.image_angle = arma_dir;
		inst.direction = arma_dir;
		inst.speed = 5;
		inst.image_yscale = xscale;
		inst.rest = ammo;
		slot[slot_selecionado] = 0;
		scr_mudar_arma(self, slot[slot_selecionado]);
	}
	
	function pegar_arma()
	{
		var inst = instance_nearest(x, y, obj_drop_arma);
		if instance_exists(inst) and distance_to_object(inst) < 50
		{
			slot[slot_selecionado] = inst.arma_index;
			scr_mudar_arma(self, slot[slot_selecionado]);
			if variable_instance_exists(inst, "rest")
			{
				ammo = inst.rest;
			}
			instance_destroy(inst);
		}
	}
	
	recoil = lerp(recoil, 0, 0.1);
	
	function reload()
	{
		if ammo = ammo_size
		{
			return false;
		}
		
		if !ammo_total > 0
		{
			return false;
		}
		
		pode_atirar = false;
		alarm[1] = carregamento;
	}
	
}else{
	instance_destroy();
}

function trocar_arma()
{

	if alarm[1] > 0
	{
		return false;
	}
	
	if slot_selecionado == 0
	{
		ammo_atual_0 = ammo;
		slot_selecionado ++;
		scr_mudar_arma(self, slot[slot_selecionado]);
		ammo = ammo_atual_1;
	}else{
		ammo_atual_1 = ammo;
		slot_selecionado--;
		scr_mudar_arma(self, slot[slot_selecionado]);
		ammo = ammo_atual_0;
	}
}




