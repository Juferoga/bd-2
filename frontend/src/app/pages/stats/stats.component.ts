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
        

        const documentStyle = getComputedStyle(document.documentElement);
        const textColor = documentStyle.getPropertyValue('--text-color');
        const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
        const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

        this.data = {
            labels: this.bestProductsData.map(product => product.nombre_producto),
            datasets: [
                {
                    label: 'Best Sellers',
                    backgroundColor: documentStyle.getPropertyValue('--blue-500'),
                    borderColor: documentStyle.getPropertyValue('--blue-500'),
                    data: this.bestSellersData.map(seller => seller.ventas_total)
                }
            ]
        };

        this.data1 = {
            labels: this.bestProductsData.map(product => product.nombre_producto),
            datasets: [
                {
                    label: 'Best Regions',
                    backgroundColor: documentStyle.getPropertyValue('--pink-500'),
                    borderColor: documentStyle.getPropertyValue('--pink-500'),
                    data: this.bestRegionData.map(region => region.ventas_total)
                }
            ]
        };

        this.data2 = {
            labels: this.bestProductsData.map(product => product.nombre_producto),
            datasets: [
                {
                    label: 'Best Products',
                    backgroundColor: documentStyle.getPropertyValue('--green-500'),
                    borderColor: documentStyle.getPropertyValue('--green-500'),
                    data: this.bestProductsData.map(product => product.cantidad_vendida)
                }
            ]
        };

        this.options = {
            indexAxis: 'y',
            maintainAspectRatio: false,
            aspectRatio: 0.8,
            plugins: {
                legend: {
                    labels: {
                        color: textColor
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: textColorSecondary,
                        font: {
                            weight: 500
                        }
                    },
                    grid: {
                        color: surfaceBorder,
                        drawBorder: false
                    }
                },
                y: {
                    ticks: {
                        color: textColorSecondary
                    },
                    grid: {
                        color: surfaceBorder,
                        drawBorder: false
                    }
                }
            }
        };
    }
    updateChartData(datasetIndex: number, data: number[]) {
        if (this.data && this.data.datasets && this.data.datasets[datasetIndex]) {
          this.data.datasets[datasetIndex].data = data;
        }
    }
}
