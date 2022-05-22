import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ForntendMainRoutingModule } from './forntend-main-routing.module';
import { ForntendMainComponent } from './forntend-main.component';
import {SharedModule} from '../shared/shared.module';
import {MaterialModule} from "../../material.module";
import {MatNativeDateModule} from "@angular/material/core";
import {FlexLayoutModule} from "@angular/flex-layout";


@NgModule({
  declarations: [
    ForntendMainComponent,
  ],
  imports: [
    CommonModule,
    ForntendMainRoutingModule,
    SharedModule,
    RouterModule,
    MatNativeDateModule,
    MaterialModule,
    FlexLayoutModule,
  ],
})
export class ForntendMainModule { }
