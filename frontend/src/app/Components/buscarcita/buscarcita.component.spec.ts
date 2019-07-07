import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BuscarcitaComponent } from './buscarcita.component';

describe('BuscarcitaComponent', () => {
  let component: BuscarcitaComponent;
  let fixture: ComponentFixture<BuscarcitaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BuscarcitaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BuscarcitaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
