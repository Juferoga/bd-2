import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddressShoppingComponent } from './address-shopping.component';

describe('AddressShoppingComponent', () => {
  let component: AddressShoppingComponent;
  let fixture: ComponentFixture<AddressShoppingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddressShoppingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddressShoppingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
