import { Component, OnInit, OnChanges } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-my-shopping',
  templateUrl: './my-shopping.component.html',
  styleUrls: ['./my-shopping.component.scss']
})
export class MyShoppingComponent implements OnInit {
  math = Math
  items: any[];
  //activeItem:any = 1;
  activeItem: MenuItem;
  ngOnInit() {
    this.items = [
        {label: 'Compra', icon: 'pi pi-fw pi-home',path:'/shopping-cart/cart'},
        {label: 'Estado', icon: 'pi pi-fw pi-calendar',path:'/shopping-cart/address'},
        {label: 'Pago', icon: 'pi pi-fw pi-pencil',path:'/shopping-cart/pay'},
    ];
    this.activeItem = this.items[0];
  }
  activeItemC(ev){
    console.log(ev);
    
  }
}
