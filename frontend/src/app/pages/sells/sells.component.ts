import { Component } from '@angular/core';
import { RepresentanteService } from 'src/app/core/services/representantes/representante.service';

@Component({
  selector: 'app-sells',
  templateUrl: './sells.component.html',
  styleUrls: ['./sells.component.scss']
})
export class SellsComponent {

  comision :any = {};

  constructor(
    private representantesService:RepresentanteService
    ) { }

  ngOnInit() {
    this.representantesService.getRepresentantesCom().subscribe(
      (data)=>{
        this.comision = data['data'];
      },
      (error)=>{
        console.log(error);
      }
    )
  }

}
