import { CrearcitaComponent } from './Components/crearcita/crearcita.component';
import { HomeComponent } from './Components/Hosp_Page/home/home.component';
import { BuscarcitaComponent } from './Components/buscarcita/buscarcita.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CrearHistorialClinicoFormComponent } from './Components/crear-historial-clinico-form/crear-historial-clinico-form.component';

const routes: Routes = [
	{
		path: 'home',
		component: HomeComponent
	},
	{
		path: 'crear-historial-clinico-form',
		component: CrearHistorialClinicoFormComponent,
	},
	{
		path: 'buscarhistorial',
		component: BuscarcitaComponent,
	},
	{
		path: 'buscarcita',
		component: BuscarcitaComponent,
	},
	{
		path: 'crearcita',
		component: CrearcitaComponent
	},

];

@NgModule({
	imports: [RouterModule.forRoot(routes)],
	exports: [RouterModule]
})
export class AppRoutingModule { }
