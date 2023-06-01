import { Injectable } from "@angular/core";
import { Subject } from "rxjs";

@Injectable()
export class TicketService {
  ticketInformation = {
    personalInformation: {
      region: "",
      pais: "",
      ciudad: "",
      direccion_entrega: ""
    },
    products: [],
    paymentInformation: {
      cardholderName: "",
      cardholderNumber: "",
      date: "",
      cvv: "",
      remember: false,
    },
  };

  private paymentComplete = new Subject<any>();

  paymentComplete$ = this.paymentComplete.asObservable();

  getTicketInformation() {
    return this.ticketInformation;
  }

  setTicketInformation(ticketInformation) {
    this.ticketInformation = ticketInformation;
  }

  complete():boolean {
    this.paymentComplete.next(this.ticketInformation.personalInformation);
    return true;
  }
}
