import { BuscarhistorialComponent } from './Components/buscarhistorial/buscarhistorial.component';
import { CrearcitaComponent } from './Components/crearcita/crearcita.component';
import { AuthService } from './Services/auth.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuNavComponent } from './Components/Hosp_Page/menu-nav/menu-nav.component';

//import primeng Module
import {ToolbarModule} from 'primeng/toolbar';
import {SplitButtonModule} from 'primeng/splitbutton';
import {SidebarModule} from 'primeng/sidebar';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {SlideMenuModule} from 'primeng/slidemenu';
import { HomeComponent } from './Components/Hosp_Page/home/home.component';
import { CrearHistorialClinicoFormComponent } from './Components/crear-historial-clinico-form/crear-historial-clinico-form.component';
import { BuscarcitaComponent } from './Components/buscarcita/buscarcita.component';
@NgModule({
  declarations: [
    AppComponent,
    MenuNavComponent,
    HomeComponent,
	CrearHistorialClinicoFormComponent,
	BuscarcitaComponent,
	CrearcitaComponent,
	BuscarhistorialComponent
  ],
  imports: [
    BrowserModule,
	AppRoutingModule,
	ToolbarModule,
	SplitButtonModule,
	SidebarModule,
	BrowserAnimationsModule,
	SlideMenuModule
  ],
  providers: [
	  AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
