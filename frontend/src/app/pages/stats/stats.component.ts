import { Component } from '@angular/core';
import { StaticsService } from 'src/app/core/services/statics/statics.service';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.scss']
})
export class StatsComponent {
    data: any;
    options: any;

    bestSellersData: any;
    bestRegionData: any;
    bestProductsData: any;
    data1: { labels: any; datasets: { label: string; backgroundColor: string; borderColor: string; data: any; }[]; };
    data2: { labels: any; datasets: { label: string; backgroundColor: string; borderColor: string; data: any; }[]; };

    constructor(
        private staticsService: StaticsService
    ) {}

    ngOnInit() {

        this.staticsService.getBestSellers('1990-01-01','2023-06-06').subscribe(
            (data)=>{
                console.log("VENDEDORES",data);
                this.bestSellersData = data.data;
            }
        )
        
        this.staticsService.getBestRegion('1990-01-01','2023-06-06').subscribe(
            (data)=>{
                console.log("REGIONES",data);
                this.bestRegionData = data.data;
            }
        )
        
        this.staticsService.getBestProducts('1990-01-01','2023-06-06').subscribe(
            (data)=>{
                console.log("PRODUCTOS",data);
                this.bestProductsData = data.data;
            }
        )
    }
}
