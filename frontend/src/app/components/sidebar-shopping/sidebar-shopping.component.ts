import { Component } from '@angular/core';
import { ICreateOrderRequest, IPayPalConfig } from 'ngx-paypal';

@Component({
  selector: 'app-sidebar-shopping',
  templateUrl: './sidebar-shopping.component.html',
  styleUrls: ['./sidebar-shopping.component.scss']
})
export class SidebarShoppingComponent {
  showSuccess: boolean = false;
  showCancel: boolean = false;
  showError: boolean = false;
  payPalConfig?: IPayPalConfig;

  constructor() { }

  /**
   * Data for test
   * email:sb-lfvyz25268036@business.example.com
   * pws: EBd3BH-ATszMw00O3-U1fGws6CvUUWJvG4QJJXM1EwqmoGX7UlbRIct4ukFdeiRdxmpsgs4H3ryxPYEx
   * Doc: https://www.npmjs.com/package/ngx-paypal
   */

  ngOnInit(): void {
    this.initConfig();
  }

  initConfig(): void {
    this.payPalConfig = {
      currency: 'USD',
      clientId: 'AYydaO0_YwGlraF1hkLDRCepcSuJFspgDzHHlz7PoLsNZ0gNvfmcspM8W_NAz1qiDgJiIEQoIFTb2Bag',
      createOrderOnClient: (data) => <ICreateOrderRequest>{
        intent: 'CAPTURE',
        purchase_units: [{
          amount: {
            currency_code: 'USD',
            value: '0.09',
            breakdown: {
              item_total: {
                currency_code: 'USD',
                value: '0.09'
              }
            }
          },
          items: [{
            name: 'Producto X',
            quantity: '1',
            category: 'PHYSICAL_GOODS',
            unit_amount: {
              currency_code: 'USD',
              value: '0.09',
            },
          }]
        }]
      },
      advanced: {
        commit: 'false'
      },
      style: {
        label: 'paypal',
        layout: 'vertical'
      },
      onApprove: (data, actions) => {
        console.log('onApprove - transaction was approved, but not authorized', data, actions);
        actions.order.get().then(details => {
          console.log('onApprove - Puedes obtener los detalles completos del pedido en el interior onApprove: ', details);
        });

      },
      onClientAuthorization: (data) => {
        console.log('onClientAuthorization - probablemente debería informar a su servidor sobre la transacción completada en este punto', data);
        this.showSuccess = true;
      },
      onCancel: (data, actions) => {
        console.log('OnCancel', data, actions);
        this.showCancel = true;

      },
      onError: err => {
        console.log('OnError', err);
        this.showError = true;
      },
      onClick: (data, actions) => {
        console.log('onClick', data, actions);
        this.resetStatus();
      }
    };
  }

  resetStatus() { }
}
