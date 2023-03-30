import { Component } from '@angular/core';
import { ShoppingService } from '@services/shopping/shopping.service';

@Component({
  selector: 'app-shopping',
  templateUrl: './shopping.component.html',
  styleUrls: ['./shopping.component.scss']
})
export class ShoppingComponent {
  data:any[]=[
    {
      k_producto: 'Producto A',
      t_nombre: 'Nombre',
      t_descripcion: 'Esta es una descripción',
      t_estado: '1',
      k_categoria: '12',
      k_pedido: '1',
      n_cantidad: 3,
      n_preciou: 38450,
      fabricante: 'fabricante',
      origen: 'Colombia',
      stock: '50',
    },
    {
      k_producto: 'Producto A',
      t_nombre: 'Nombre',
      t_descripcion: 'Esta es una descripción',
      t_estado: '1',
      k_categoria: '12',
      k_pedido: '1',
      n_cantidad: 3,
      n_preciou: 38450,
      fabricante: 'fabricante',
      origen: 'Colombia',
      stock: '50',
    },
    {
      k_producto: 'Producto A',
      t_nombre: 'Nombre',
      t_descripcion: 'Esta es una descripción',
      t_estado: '1',
      k_categoria: '12',
      k_pedido: '1',
      n_cantidad: 3,
      n_preciou: 38450,
      fabricante: 'fabricante',
      origen: 'Colombia',
      stock: '50',
    },
    {
      k_producto: 'Producto A',
      t_nombre: 'Nombre',
      t_descripcion: 'Esta es una descripción',
      t_estado: '1',
      k_categoria: '12',
      k_pedido: '1',
      n_cantidad: 3,
      n_preciou: 38450,
      fabricante: 'fabricante',
      origen: 'Colombia',
      stock: '50',
    },
  ]
  total:number=0;

  constructor(private shoppingService:ShoppingService){

    this.data.map(el =>{
      this.total = this.total + (el.n_cantidad * el.n_preciou)
    })
    // Se agregan los productos al carrito
    this.shoppingService.shoppingCart.subscribe({
      next:(response)=>{
        this.data.push(response)
      },
      complete:()=>{
        this.calcTotal()
      },
      error:(err)=>{},
    });
  }

  //Proceso para eliminar producto del carrito
  deleteProduct(item){
    let index = this.data.findIndex(el => el['k_producto'] === item['k_producto'])
    this.data.splice(index,1)
    //this.shoppingService.sendproduct(this.data)
    this.calcTotal()
  }

  calcTotal(){
    this.data.map(el =>{
      this.total = this.total + (el.n_cantidad * el.n_preciou)
    })
  }
}
