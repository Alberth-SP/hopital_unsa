import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearHistorialClinicoFormComponent } from './crear-historial-clinico-form.component';

describe('CrearHistorialClinicoFormComponent', () => {
  let component: CrearHistorialClinicoFormComponent;
  let fixture: ComponentFixture<CrearHistorialClinicoFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CrearHistorialClinicoFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CrearHistorialClinicoFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});