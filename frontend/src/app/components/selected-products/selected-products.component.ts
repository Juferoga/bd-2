import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-selected-products',
  templateUrl: './selected-products.component.html',
  styleUrls: ['./selected-products.component.scss']
})
export class SelectedProductsComponent {
  @Input() data:any[];
  @Output() deleteitem: EventEmitter<any> = new EventEmitter();

  deleteProduct(){
    this.deleteitem.emit()
  }
}
