import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TicketService } from 'src/app/core/services/compra/ticket.service';

@Component({
    template: `
        <div class="stepsdemo-content">
            <p-card>
                <ng-template pTemplate="title"> Productos  </ng-template>
                <ng-template pTemplate="subtitle"> Elige tus productos </ng-template>
                <ng-template pTemplate="content">
                    <!-- TODO: TABLA PARA SELECCIONAR PRODUCTOS -->
                    
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
    constructor(public ticketService: TicketService, private router: Router) {}

    products: any;
    productList;

    ngOnInit() {
        this.products = this.ticketService.ticketInformation.products;

    }
    
    nextPage() {
        this.ticketService.ticketInformation.products = this.products;
        this.router.navigate(['admin/mis-compras/payment']);
    }

    prevPage() {
        this.router.navigate(['admin/mis-compras/personal']);
    }
}