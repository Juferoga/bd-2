import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment.development';

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.scss']
})
export class SideBarComponent{
  public href: string = "";
  api = environment.api;
  
  constructor(private router: Router) {}

  ngOnInit() {
    this.href = this.router.url.includes("admin")? '/admin':'/app';
  }
}
