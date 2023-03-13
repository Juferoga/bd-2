import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

declare let paypal;

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.scss']
})
export class PaymentComponent implements OnInit{
  @ViewChild('paypal', {static:true}) paypalElement: ElementRef;
  product ={
    description: '',
    price:4500.23,
    img: '',
  }
  constructor(){}

  /**
   * Data for test
   * email:sb-lfvyz25268036@business.example.com
   * pws: EP1ecT91YB2Pfs40Avm30OBgWmf54HqdMeg1rvRk_s6ay9jXNvE7Y5cgNk_9aSljYjtXPfiE7pD4asGi
   */
  ngOnInit(): void {
    paypal.Buttons({
      createOrder:(data, actions)=>{
        return actions.order.create({
          purchase_units:[
            {
              description:this.product.description,
              amount:{
                currency_code: 'COL',
                value: this.product.price
              }
            }
          ]
        })
      },
      onApprove: async(data,actions) =>{
        const order = await actions.order.capture()
        console.log(order);
      },
      onError:(err) =>{
        console.log(err);
      }
    }).render(this.paypalElement.nativeElement);
  }
}
