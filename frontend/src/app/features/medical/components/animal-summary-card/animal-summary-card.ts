import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-animal-summary-card',
  standalone: true,
  templateUrl: './animal-summary-card.html',
  styleUrl: './animal-summary-card.scss'
})
export class AnimalSummaryCardComponent {

  @Input() animal: any;

}