import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TicketService } from 'src/app/core/services/compra/ticket.service';

@Component({
    template: `
        <div class="stepsdemo-content">
            <p-card>
                <ng-template pTemplate="title"> Confirmación </ng-template>
                <ng-template pTemplate="subtitle"> Confirma tu compra </ng-template>
                <ng-template pTemplate="content">
                    <div class="field col-12">
                        <label for="class">Region</label>
                        <b>{{ ticketInformation.personalInformation.region }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="class">País</label>
                        <b>{{ ticketInformation.personalInformation.pais }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="class">Ciudad</label>
                        <b>{{ ticketInformation.personalInformation.ciudad }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="class">Dirección de entrega</label>
                        <b>{{ ticketInformation.personalInformation.direccion_entrega }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">Seat Class</label>
                        <b>{{ ticketInformation.seatInformation.class ? ticketInformation.seatInformation.class.name : '-' }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">Wagon Number</label>
                        <b>{{ ticketInformation.seatInformation.wagon ? ticketInformation.seatInformation.wagon.wagon : '-' }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">Seat</label>
                        <b>{{ ticketInformation.seatInformation.seat ? ticketInformation.seatInformation.seat.seat : '-' }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">Cardholder Name</label>
                        <b>{{ ticketInformation.paymentInformation.cardholderName ? ticketInformation.paymentInformation.cardholderName : '-' }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">Card Number</label>
                        <b>{{ ticketInformation.paymentInformation.cardholderNumber ? ticketInformation.paymentInformation.cardholderNumber : '-' }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">Date</label>
                        <b>{{ ticketInformation.paymentInformation.date ? ticketInformation.paymentInformation.date : '-' }}</b>
                    </div>
                    <div class="field col-12">
                        <label for="Age">CVV</label>
                        <b>{{ ticketInformation.paymentInformation.cvv && ticketInformation.paymentInformation.cvv.length === 3 ? '**' + ticketInformation.paymentInformation.cvv[2] : '-' }}</b>
                    </div>
                </ng-template>
                <ng-template pTemplate="footer">
                    <div class="grid grid-nogutter justify-content-between">
                        <p-button label="Volver" (onClick)="prevPage()" icon="pi pi-angle-left"></p-button>
                        <p-button label="Completar" (onClick)="complete()" icon="pi pi-angle-right" iconPos="right" styleClass="p-button-success"></p-button>
                    </div>
                </ng-template>
            </p-card>
        </div>
    `
})
export class ConfirmationDemo implements OnInit {
    ticketInformation: any;

    constructor(public ticketService: TicketService, private router: Router) {}

    ngOnInit() {
        this.ticketInformation = this.ticketService.ticketInformation;
    }

    complete() {
        this.ticketService.complete();
    }

    prevPage() {
        this.router.navigate(['admin/mis-compras/payment']);
    }
}