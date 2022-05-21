import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ForntendMainComponent } from './forntend-main.component';

describe('ForntendMainComponent', () => {
  let component: ForntendMainComponent;
  let fixture: ComponentFixture<ForntendMainComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ForntendMainComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ForntendMainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
