import { Component, OnInit, OnChanges } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-my-shopping',
  templateUrl: './my-shopping.component.html',
  styleUrls: ['./my-shopping.component.scss']
})
export class MyShoppingComponent implements OnInit {
  math = Math
  items: MenuItem[];
  activeItem = 1;

  ngOnInit() {
    this.items = [
        {label: 'Compra', icon: 'pi pi-fw pi-home',},
        {label: 'Estado', icon: 'pi pi-fw pi-calendar'},
        {label: 'Pago', icon: 'pi pi-fw pi-pencil'},
    ];
  }

}
