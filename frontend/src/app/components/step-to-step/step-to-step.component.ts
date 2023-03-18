import { Component, ViewEncapsulation } from '@angular/core';
import { MenuItem, MessageService } from 'primeng/api';

@Component({
  selector: 'app-step-to-step',
  providers: [MessageService],
  templateUrl: './step-to-step.component.html',
  styleUrls: ['./step-to-step.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class StepToStepComponent {
  items: MenuItem[];

  activeIndex: number = 1;

  constructor(private messageService: MessageService) { }

  ngOnInit() {
    this.items = [{
      label: 'Carrito de compras',
      command: (event: any) => {
        this.activeIndex = 0;
        this.messageService.add({ severity: 'info', summary: 'Carrito de compras', detail: event.item.label });
      }
    },
    {
      label: 'Información de envío',
      command: (event: any) => {
        this.activeIndex = 1;
        this.messageService.add({ severity: 'info', summary: 'Información de envío', detail: event.item.label });
      }
    },
    {
      label: 'Pago',
      command: (event: any) => {
        this.activeIndex = 2;
        this.messageService.add({ severity: 'info', summary: 'Pago', detail: event.item.label });
      }
    },
    ];
  }
}
