import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.scss','../admin/admin.component.scss']
})
export class ShoppingCartComponent implements OnInit {
  items: MenuItem[];

  ngOnInit() {
    this.items = [
        {label: 'Compra', icon: 'pi pi-fw pi-home'},
        {label: 'Estado', icon: 'pi pi-fw pi-calendar'},
        {label: 'Pago', icon: 'pi pi-fw pi-pencil'},
    ];
}

}
