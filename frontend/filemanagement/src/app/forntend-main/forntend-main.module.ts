import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ForntendMainRoutingModule } from './forntend-main-routing.module';
import { ForntendMainComponent } from './forntend-main.component';
import {SharedModule} from '../shared/shared.module';


@NgModule({
  declarations: [
    ForntendMainComponent,
  ],
  imports: [
    CommonModule,
    ForntendMainRoutingModule,
    SharedModule,
    RouterModule,
  ],
})
export class ForntendMainModule { }
