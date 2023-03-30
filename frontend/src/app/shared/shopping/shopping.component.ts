import { Component, OnInit } from '@angular/core';
import { ShoppingService } from '@services/shopping/shopping.service';

@Component({
  selector: 'app-shopping',
  templateUrl: './shopping.component.html',
  styleUrls: ['./shopping.component.scss']
})
export class ShoppingComponent implements OnInit {
  data:any[]=[
    {
      k_producto: 'Producto A',
      t_nombre: 'Nombre',
      t_descripcion: 'Esta es una descripción',
      t_estado: '1',
      k_categoria: '12',
      k_pedido: '1',
      n_cantidad: 1,
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
      n_cantidad: 1,
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
      n_cantidad: 1,
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
      n_cantidad: 1,
      n_preciou: 38450,
      fabricante: 'fabricante',
      origen: 'Colombia',
      stock: '50',
    }
  ]
  total:number=0;

  constructor(private shoppingService:ShoppingService){
    // Se agregan los productos al carrito
    this.shoppingService.shoppingCart.subscribe({
      next:(response)=>{
        if(response) this.data.push(response)
      },
      complete:()=>{ 
      },
      error:(err)=>{},
    });
  }
  
  ngOnInit(): void {
    this.calcTotal()
  }

  //Proceso para eliminar producto del carrito
  deleteProduct(item){
    let index = this.data.findIndex(el => el['k_producto'] === item['k_producto'])
    this.data.splice(index,1)
    this.calcTotal()
  }

  calcTotal(){
    this.total = 0
    this.data.map(el =>{
      this.total = this.total + (parseInt(el.n_cantidad) * el.n_preciou)
    })
  }
}
