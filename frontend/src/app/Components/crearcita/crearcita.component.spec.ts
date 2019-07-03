import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearcitaComponent } from './crearcita.component';

describe('CrearcitaComponent', () => {
  let component: CrearcitaComponent;
  let fixture: ComponentFixture<CrearcitaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CrearcitaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CrearcitaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
