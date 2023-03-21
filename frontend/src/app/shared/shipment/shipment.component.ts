import { Component } from '@angular/core';

@Component({
  selector: 'app-shipment',
  templateUrl: './shipment.component.html',
  styleUrls: ['./shipment.component.scss']
})
export class ShipmentComponent {

  // TODO: Mejorar xD, programar dormido be like... 

  isDelivered:boolean = false;
  isArrived:boolean = false;
  isInProgress:boolean = false;

  getStatus():string{
    if(this.isDelivered){ return "Tú pedido esta en camino" }
    else{
      if(this.isArrived){ return "Tú pedido ha llegado" }
      else{ 
        if(this.isInProgress){ return "Tú pedido está en progreso" }
        else{ 
          return "Tú pedido esta en el limbo" 
        }
      }
    }
  }
}
