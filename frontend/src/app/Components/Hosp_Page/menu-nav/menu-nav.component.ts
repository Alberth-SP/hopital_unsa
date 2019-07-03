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
				command: (onclick)=> {console.log("funciona xD")},
				items: [
					{
						label: 'Buscar Historial',
						icon: 'pi pi-search',
						routerLink:['./buscarhistorial'],
						command: (onclick)=> {console.log("Buscar xD")}

						
					},
					{
					label: 'Buscar Historia Clinica',
					icon: 'pi pi-search',
					routerLink:['./buscarhistorial']
					
				},
				{ label: 'Crear Historia Clinica' },
				{ separator: true },
				{ label: 'Quit' },
				
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
				command: (onclick)=> {console.log("funcion 2a xD")},
				routerLink:['/home']
			}
		];
	}


}
