import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { Product } from 'src/app/core/models/products/product.model';
import { BodegaService } from 'src/app/core/services/bodegas/bodega.service';
import { TicketService } from 'src/app/core/services/compra/ticket.service';
import { OrderService } from 'src/app/core/services/order/order.service';
import { ProductService } from 'src/app/core/services/products/product.service';

@Component({
    template: `
        <div class="stepsdemo-content">
            <p-card>
                <ng-template pTemplate="title"> Productos  </ng-template>
                <ng-template pTemplate="subtitle"> Elige tus productos </ng-template>
                <ng-template pTemplate="content">
                <p-table [value]="productList" dataKey="code" [tableStyle]="{'min-width': '50rem'}">
                    <ng-template pTemplate="header">
                        <tr>
                            <th style="width: 4rem">
                                No.
                            </th>
                            <th>Nombre</th>
                            <th>Descripción</th>
                            <th>Precio</th>
                            <th>Cantidad</th>
                            <th>Categoría</th>
                        </tr>
                    </ng-template>
                    <ng-template pTemplate="body" let-product let-a>
                        <tr>
                            <td><pre>{{a.id}}</pre></td>
                            <td>{{product.nombre}}</td>
                            <td>{{product.descripcion}}</td>
                            <td>{{product.precio}}</td>
                            <td>{{product.cantidad}}</td>
                            <td style="display: flex; justify-content: space-evenly;">
                                <p-button (click)="agregarCarrito(a.id,product)" icon="pi pi-plus" styleClass="p-button-rounded"></p-button>
                                <p-button (click)="eliminarCarrito(a.id)" icon="pi pi-minus" styleClass="p-button-rounded"></p-button>
                            </td>
                        </tr>
                    </ng-template>
                </p-table>
                </ng-template>
                <ng-template pTemplate="footer">
                    <div class="grid grid-nogutter justify-content-between">
                        <p-button label="Volver" (onClick)="prevPage()" icon="pi pi-angle-left"></p-button>
                        <p-button label="Siguiente" (onClick)="nextPage()" icon="pi pi-angle-right" iconPos="right"></p-button>
                    </div>
                </ng-template>
            </p-card>
        </div>
        `
})
export class SeatDemo implements OnInit {
    constructor(
        public ticketService: TicketService, 
        private router: Router,
        private messageService: MessageService,
        private productService: ProductService,
        private orderService:OrderService,
				private bodegaService:BodegaService) {}

    products: any;
    productList : Product[];
    productListCarrito : Product[];

    ngOnInit() {
        this.products = this.ticketService.ticketInformation.products;
				let url = ''
				// Construir la parte de la URL correspondiente a las variables existentes
				let urlParams = '';
				let warehouse = 3
				if (this.ticketService.ticketInformation.personalInformation.pais) {
					urlParams += 'c';
					url += `?country=${this.ticketService.ticketInformation.personalInformation.pais}`;
				}
				if (this.ticketService.ticketInformation.personalInformation.region) {
					urlParams += 'r';
					url += `${urlParams === '' ? '?' : '&'}region=${this.ticketService.ticketInformation.personalInformation.region}`;
				}
				if (warehouse) {
					urlParams += 'h';
					url += `${urlParams === '' ? '?' : '&'}warehouse=${warehouse}`;
				}

				// Añadir la parte de la URL correspondiente a las variables existentes
				url = `${urlParams}/${url}`;  
				this.bodegaService.getBodegaInventory(url).subscribe({
					next: (response) => {
						this.productList = response["data"];
						this.messageService.add({
							key: "grl-toast",
							severity: "success",
							summary: "Consulta exitosa",
							detail: `La consulta de la BODEGA ${url} se realizo correctamente sobre la base de datos`,
						});
					},
					error: (err) => {
						this.messageService.add({
							key: "grl-toast",
							severity: "error",
							summary: `Consulta de la BODEGA ${url} realizada SIN ÉXITO`,
							detail: "::: ERROR ::: \n" + err["error"]["detail"],
						});
					}
				});
    }
    
    nextPage() {
        this.ticketService.ticketInformation.products = this.products;
        this.router.navigate(['admin/mis-compras/payment']);
    }

    prevPage() {
        this.router.navigate(['admin/mis-compras/personal']);
    }

    agregarCarrito(id,product){
			let data = {
				id_producto: id,
				id_pedido: 3265,
				cantidad: product.cantidad,
				precio_unitario: product.precio
			}
        this.orderService.addItemOrder(data).subscribe(
            (data)=> {
                this.productListCarrito = data['data'];
            },
            (err)=>{
                this.messageService.add({
                    key: "grl-toast",
                    severity: "error",
                    summary: "ERROR",
                    detail: "La consulta se realizo con errores"+err,
                });
            }
        )
    }

    eliminarCarrito(id){

    }
}