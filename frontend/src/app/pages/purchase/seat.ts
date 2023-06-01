import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { Product } from 'src/app/core/models/products/product.model';
import { TicketService } from 'src/app/core/services/compra/ticket.service';
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
                                <p-tableHeaderCheckbox></p-tableHeaderCheckbox>
                            </th>
                            <th>Nombre</th>
                            <th>Descripción</th>
                            <th>Precio</th>
                            <th>Cantidad</th>
                            <th>Categoría</th>
                        </tr>
                    </ng-template>
                    <ng-template pTemplate="body" let-product>
                        <tr>
                            <td>
                                <p-tableCheckbox [value]="product"></p-tableCheckbox>
                            </td>
                            <td>{{product.nombre}}</td>
                            <td>{{product.descripcion}}</td>
                            <td>{{product.precio}}</td>
                            <td>{{product.cantidad}}</td>
                            <td>
                                
                                
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
        private productService: ProductService) {}

    products: any;
    productList : Product[];

    ngOnInit() {
        this.products = this.ticketService.ticketInformation.products;
        this.productService.getProductS2(this.ticketService.ticketInformation.personalInformation.pais, this.ticketService.ticketInformation.personalInformation.region).subscribe(
            (data)=>{
                this.productList = data['data'];
                this.messageService.add({
                    key: "grl-toast",
                    severity: "success",
                    summary: "Consulta exitosa",
                    detail: "La consulta se realizo correctamente sobre la base de datos - Países Cargados",
                });
            },
            (error)=>{
                this.messageService.add({
                    key: "grl-toast",
                    severity: "error",
                    summary: "ERROR",
                    detail: "La consulta se realizo con errores"+error,
                });
            }
        )
    }
    
    nextPage() {
        this.ticketService.ticketInformation.products = this.products;
        this.router.navigate(['admin/mis-compras/payment']);
    }

    prevPage() {
        this.router.navigate(['admin/mis-compras/personal']);
    }
}