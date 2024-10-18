// Os recursos de script mudaram para a v2.3.0; veja
// https://help.yoyogames.com/hc/en-us/articles/360005277377 para obter mais informações
function scr_mudar_arma(_id, index){

arma = index;
var map = _id.armas[_id.arma];
_id.melee = map[? "melee"];
_id.sprite = map[? "sprite"];
_id.proj = map[? "proj"];
_id.proj_count = map[? "proj_count"];
_id.proj_spd = map[? "proj_spd"];
_id.proj_damage = map[? "proj_damage"];
_id.proj_delay = map[? "proj_delay"];
_id.automatic = map[? "automatic"];
_id.drop = map[? "drop"];
_id.ammo = map[? "ammo"];
_id.ammo_size = map[? "ammo_size"];
_id.carregamento = map[? "carregamento"];
_id.stealth = map[? "stealth"];

}