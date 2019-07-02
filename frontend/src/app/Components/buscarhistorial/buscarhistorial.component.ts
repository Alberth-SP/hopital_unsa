import { Component, OnInit } from '@angular/core';
import {NgModule}     from '@angular/core';
import {RouterModule} from '@angular/router';

@Component({
  selector: 'app-buscarhistorial',
  templateUrl: './buscarhistorial.component.html',
  styleUrls: ['./buscarhistorial.component.css']
})
export class BuscarhistorialComponent implements OnInit {

  paciente:string;
  dni:string;
  crear:string;

  constructor() {
    this.paciente=" ";
    this.dni=" ";
    this.crear=" ";
   }

  ngOnInit() {
  } 
  clickbuscar(){
    
        alert("Buscando ... ");
        this.paciente="PACIENTE";
        this.dni="DNI";
        this.crear="Crear Cita";
  }

  clickcrear(){
    alert("Crear Cita")
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
   