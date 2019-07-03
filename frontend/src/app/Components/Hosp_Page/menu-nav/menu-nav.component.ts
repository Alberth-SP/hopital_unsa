import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
	selector: 'app-menu-nav',
	templateUrl: './menu-nav.component.html',
	styleUrls: ['./menu-nav.component.css']
})
export class MenuNavComponent implements OnInit {
	items: MenuItem[];
	constructor() { }

	ngOnInit() {
		this.items = [
			{
				label: 'Modulo Admision',
				icon: 'pi pi-fw pi-file',
				command: (onclick) => { console.log("funciona xD") },
				items: [{
					label: 'Historial',

					items: [
						{
							label: 'Buscar Historia Clinica',
							icon: 'pi pi-search',
							routerLink: ['/buscarhistorial']
						},
						{
							label: 'Crear Historia Clinica',
							routerLink: ['/crear-historial-clinico-form']
						},
						{ separator: true },
					]
				},
				//Submenu de Cita 
				{
					label: 'Citas',

					items: [
						{
							label: 'Busqueda de Citas',
							icon: 'pi pi-search',
							routerLink: ['/buscarcita']
						},
						{
							label: 'Crear Cita',
							routerLink: ['/crearcita']
						},
					]
				}

				]
			},
			{
				label: 'Modulo Consultorio',
				//se pueden usar iconode de font awesome o primeng
				icon: 'pi pi-fw pi-pencil',
			},
			{
				label: 'Modulo Laboratorio',
				icon: 'pi pi-fw pi-question',
			},
			{
				label: 'Modulo Triaje',
				icon: 'pi pi-fw pi-cog',
			},
			{ separator: true },
			// ejemplo de tuteo desde el menu, antes deben agregarlos en app-routing.module
			{
				label: 'Home', icon: 'pi pi-fw pi-times',
				routerLink: ['/home']
			}
		];
	}


}
