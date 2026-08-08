import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';

import {
  /*LucideIconComponent,*/
  LucideHouse,
  LucidePawPrint,
  LucideHeartPulse,
  LucideBaby,
  LucideTriangleAlert,
  LucideChartColumn,
  LucideUser,
  LucideHistory
} from '@lucide/angular';
@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    RouterLinkActive,
    /*LucideIconComponent*/
    
  ],
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {
  /*readonly House = LucideHouse;
  readonly PawPrint = LucidePawPrint;
  readonly HeartPulse = LucideHeartPulse;
  readonly Baby = LucideBaby;
  readonly TriangleAlert = LucideTriangleAlert;
  readonly ChartColumn = LucideChartColumn;
  readonly User = LucideUser;
  readonly History = LucideHistory;*/
}