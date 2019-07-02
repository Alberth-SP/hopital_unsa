import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BuscarhistorialComponent } from './buscarhistorial.component';

describe('BuscarhistorialComponent', () => {
  let component: BuscarhistorialComponent;
  let fixture: ComponentFixture<BuscarhistorialComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BuscarhistorialComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BuscarhistorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
