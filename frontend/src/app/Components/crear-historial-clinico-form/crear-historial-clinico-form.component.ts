import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-crear-historial-clinico-form',
  templateUrl: './crear-historial-clinico-form.component.html',
  styleUrls: ['./crear-historial-clinico-form.component.css']
})
export class CrearHistorialClinicoFormComponent implements OnInit {
  name:string;
  dni:string;
  pBirth:string;
  dBirth:string;
  age:number;
  phone:string;
  gender:string;
  address:string;
  neighb:string;
  relation:string;
  grade:string;
  job:string;
  origin:string;
  dCurrent:string;

  constructor() {
    this.name="";
    this.dni="";
    this.pBirth="";
    this.dBirth="";
    this.age=0;
    this.phone="";
    this.gender="";
    this.address="";
    this.neighb="";
    this.relation="";
    this.grade="";
    this.job="";
    this.origin="";
    this.dCurrent="";
  }

  ngOnInit() {
  }
  crearHitoria(){
    //INSERT ___ from ____
  }

}
