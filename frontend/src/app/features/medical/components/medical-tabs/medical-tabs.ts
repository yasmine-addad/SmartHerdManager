import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-medical-tabs',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './medical-tabs.html',
  styleUrl: './medical-tabs.scss'
})
export class MedicalTabsComponent {

  active = "vaccinations";

  @Output()
  change = new EventEmitter<string>();

  tabs = [
    {
      label: "Vaccinations",
      value: "vaccinations"
    },
    {
      label: "Maladies",
      value: "maladies"
    },
    {
      label: "Traitements",
      value: "traitements"
    },
    {
      label: "Visites vétérinaires",
      value: "visites"
    }
  ];

  select(tab: string) {

    this.active = tab;
    this.change.emit(tab);

  }

}