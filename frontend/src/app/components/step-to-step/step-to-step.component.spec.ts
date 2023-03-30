import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StepToStepComponent } from './step-to-step.component';

describe('StepToStepComponent', () => {
  let component: StepToStepComponent;
  let fixture: ComponentFixture<StepToStepComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StepToStepComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StepToStepComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
