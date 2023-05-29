import { Component } from '@angular/core';
import { MenuItem, MessageService } from 'primeng/api';
import { Subscription } from 'rxjs';
import { TicketService } from 'src/app/core/services/compra/ticket.service';

@Component({
  selector: 'app-purchase',
  templateUrl: './purchase.component.html',
  styleUrls: ['./purchase.component.scss']
})
export class PurchaseComponent {
  items: MenuItem[];

    subscription: Subscription;

    constructor(
      public messageService: MessageService, 
      public ticketService: TicketService
    ) {}

    ngOnInit() {
        this.items = [
            {
                label: 'Información personal',
                routerLink: 'personal'
            },
            {
                label: 'Productos',
                routerLink: 'seat'
            },
            {
                label: 'Pago',
                routerLink: 'payment'
            },
            {
                label: 'Confirmación',
                routerLink: 'confirmation'
            }
        ];

        this.subscription = this.ticketService.paymentComplete$.subscribe((personalInformation) => {
            this.messageService.add({ severity: 'success', summary: 'Order submitted', detail: 'Dear, ' + personalInformation.firstname + ' ' + personalInformation.lastname + ' your order completed.' });
        });
    }

    ngOnDestroy() {
        if (this.subscription) {
            this.subscription.unsubscribe();
        }
    }
}
