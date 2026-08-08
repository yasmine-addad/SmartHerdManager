import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-medical-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './medical-table.html',
  styleUrl: './medical-table.scss'
})
export class MedicalTableComponent {

  @Input()
  columns: string[] = [];

  @Input()
  data: any[] = [];

}