import { HomeComponent } from './Components/Hosp_Page/home/home.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BuscarhistorialComponent } from './Components/buscarhistorial/buscarhistorial.component';

const routes: Routes = [
	{
		path:'home',
		component: HomeComponent
	},
	{
		path:'buscarhistorial',
		component: BuscarhistorialComponent,
	}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
