import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TicketService } from 'src/app/core/services/compra/ticket.service';

@Component({
    template: `
        <div class="stepsdemo-content">
            <p-card>
                <ng-template pTemplate="title"> Información de pago </ng-template>
                <ng-template pTemplate="subtitle"> Ingresa los detalles de tu pago </ng-template>
                <ng-template pTemplate="content">
                    <div class="p-fluid formgrid grid">
                        <div class="field col-12">
                            <label for="class">Nombre del propietario de la tarjeta</label>
                            <input type="text" required pInputText [(ngModel)]="paymentInformation.cardholderName" />
                        </div>
                        <div class="field col-8">
                            <label id="number" for="lastname">Número</label>
                            <p-inputMask inputId="number" mask="9999-9999-9999-9999" [(ngModel)]="paymentInformation.cardholderNumber"></p-inputMask>
                        </div>
                        <div class="field col-2">
                            <label id="date" for="date">Fecha de vencimiento</label>
                            <p-inputMask inputId="date" mask="99/99" [(ngModel)]="paymentInformation.date"></p-inputMask>
                        </div>
                        <div class="field col-2">
                            <label for="cvv">CCV</label>
                            <p-inputMask id="cvv" mask="999" [(ngModel)]="paymentInformation.cvv"></p-inputMask>
                        </div>
                        <div class="field-checkbox col-12">
                            <p-checkbox id="remember" [binary]="true" [(ngModel)]="paymentInformation.remember"></p-checkbox>
                            <label for="remember" class="p-checkbox-label">Agrega está tarjeta para futuras compras.</label>
                        </div>
                    </div>
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
export class PaymentDemo implements OnInit {
    paymentInformation: any;

    constructor(public ticketService: TicketService, private router: Router) {}

    ngOnInit() {
        this.paymentInformation = this.ticketService.ticketInformation.paymentInformation;
    }

    nextPage() {
        this.ticketService.ticketInformation.paymentInformation = this.paymentInformation;
        this.router.navigate(['admin/mis-compras/confirmation']);
    }

    prevPage() {
        this.router.navigate(['admin/mis-compras/seat']);
    }
}