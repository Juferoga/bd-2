import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PaymentShoppingComponent } from './payment-shopping.component';

describe('PaymentShoppingComponent', () => {
  let component: PaymentShoppingComponent;
  let fixture: ComponentFixture<PaymentShoppingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PaymentShoppingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PaymentShoppingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
