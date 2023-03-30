import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SidebarShoppingComponent } from './sidebar-shopping.component';

describe('SidebarShoppingComponent', () => {
  let component: SidebarShoppingComponent;
  let fixture: ComponentFixture<SidebarShoppingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SidebarShoppingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SidebarShoppingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
