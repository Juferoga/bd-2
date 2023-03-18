import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PurchaseProcessCardComponent } from './purchase-process-card.component';

describe('PurchaseProcessCardComponent', () => {
  let component: PurchaseProcessCardComponent;
  let fixture: ComponentFixture<PurchaseProcessCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PurchaseProcessCardComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PurchaseProcessCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
