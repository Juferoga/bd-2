import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { Messages } from 'primeng/messages';
import { TicketService } from 'src/app/core/services/compra/ticket.service';
import { OrderService } from 'src/app/core/services/order/order.service';

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
        
        <p-dialog header="Califica tu experiencia" [(visible)]="visible" [modal]="true" [style]="{ width: '50vw' }" [draggable]="false" [resizable]="false">
            <p class="m-0">
                Tú experiencia es muy importante para nosotros, selecciona qu e tan contento estas con el maneo del tramite!!!
            </p>

            <p-rating [(ngModel)]="cal.calificacion" [stars]="5" [cancel]="false">
                <ng-template pTemplate="onicon">
                    <img src="https://primefaces.org/cdn/primeng/images/demo/rating/custom-icon-active.png" width="25px" height="25px" />
                </ng-template>
                <ng-template pTemplate="officon">
                    <img src="https://primefaces.org/cdn/primeng/images/demo/rating/custom-icon.png" width="25px" height="25px" />
                </ng-template>
            </p-rating>
            <textarea [(ngModel)]="cal.observacion" rows="5" cols="30" pInputTextarea ></textarea>

            <p-button style="display: flex; align-items;justify-content: flex-end;" (click)="sendRating()" icon="pi pi-external-link" label="Enviar"></p-button>
        </p-dialog>
    `
})
export class ConfirmationDemo implements OnInit {
    ticketInformation: any;
    cal : any = {'calificacion':0,'observacion':''};
    visible = false;

    constructor(
        public ticketService: TicketService, 
        private router: Router,
        private orderService:OrderService,
        private messageService:MessageService) {}

    ngOnInit() {
        this.ticketInformation = this.ticketService.ticketInformation;
    }

    complete() {
        this.visible = this.ticketService.complete();
        
    }
    
    prevPage() {
        this.router.navigate(['admin/mis-compras/payment']);
    }
    
    showDialog() {
        this.visible = true;
    }
    
    sendRating() {
        this.orderService.rateOrder(this.cal).subscribe(
            (data)=>{
                this.messageService.add({
                    key: "grl-toast",
                    severity: "success",
                    summary: "Consulta exitosa",
                    detail: "La consulta se realizo correctamente sobre la base de datos - Países Cargados",
                });
                this.visible = false; 
            },
            (error)=>{
                this.messageService.add({
                    key: "grl-toast",
                    severity: "error",
                    summary: "ERROR",
                    detail: "La consulta se realizo con errores"+error['detail'],
                });
            }
        )
    }

}