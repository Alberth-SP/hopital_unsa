import { Component, OnInit } from '@angular/core';
import {NgModule}     from '@angular/core';
import {RouterModule} from '@angular/router';

@Component({
  selector: 'app-buscarcita',
  templateUrl: './buscarcita.component.html',
  styleUrls: ['./buscarcita.component.css']
})
export class BuscarcitaComponent implements OnInit {

  paciente:string;
  dni:string;
  especialidad:string;
  fecha:string; 

  constructor() {
    this.paciente=" ";
    this.dni=" ";
    this.especialidad=" ";
    this.fecha=" "; 
   }


  ngOnInit() {
  } 
  clickbuscar(){
    
        alert("Buscando ... ");
        this.paciente="PACIENTE";
        this.dni="DNI";
        this.especialidad="MEDICINA";
        this.fecha="FECHA" ; 
  }

 
}





/*
export class HomeComponent implements OnInit {
  
    datos;
  
    opcionSeleccionado: string  = '0'; // Iniciamos
    verSeleccion: string        = '';
 
   constructor() { 
    this.datos = [1,2,3,4,5,6,7,8,9,10];
    }
 
   ngOnInit() {
   }
 
   clickbuscar(){
 
     alert("Buscando ... ");
      
   }
   capturar() {
    
        this.verSeleccion = this.opcionSeleccionado;
      }
    }*/
   