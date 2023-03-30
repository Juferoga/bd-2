import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-selected-products',
  templateUrl: './selected-products.component.html',
  styleUrls: ['./selected-products.component.scss']
})
export class SelectedProductsComponent implements OnInit{
  @Input() data:any[];
  @Output() deleteitem: EventEmitter<any> = new EventEmitter();
  @Output() reCalculate: EventEmitter<any> = new EventEmitter();
  total:number = 0;

  ngOnInit(){    
    this.updateValueTotal(this.data['n_cantidad'])
  }

  deleteProduct(){
    this.deleteitem.emit()
  }

  updateValueTotal(cant){
    this.total = this.data['n_preciou']*cant
    this.reCalculate.emit()
  }
}
