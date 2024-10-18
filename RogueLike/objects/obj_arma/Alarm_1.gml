/// @description Inserir descrição aqui
// Você pode escrever seu código neste editor

pode_atirar = true;

var qtd = ammo_size - ammo;
if ammo_total > qtd
{
	ammo += qtd;
	ammo_total -= qtd;
}else{
	ammo += ammo_total;
	ammo_total = 0;
}







