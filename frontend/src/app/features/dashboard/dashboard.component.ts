import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnimalService } from '../../core/services/animal.service';
import { AlertService } from '../../core/services/alert.service';
import { Animal } from '../../shared/models/animal.model';
import { Alert } from '../../shared/models/alert.model';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
})
export class DashboardComponent implements OnInit {
  readonly animals = signal<Animal[]>([]);
  readonly alerts = signal<Alert[]>([]);
  readonly isLoading = signal(true);

  constructor(
    private readonly animalService: AnimalService,
    private readonly alertService: AlertService,
  ) {}

  ngOnInit(): void {
    this.animalService.getAll().subscribe((animals) => this.animals.set(animals));
    this.alertService.getAll().subscribe((alerts) => {
      this.alerts.set(alerts);
      this.isLoading.set(false);
    });
  }

  get activeAnimalsCount(): number {
    return this.animals().filter((a) => a.status === 'active').length;
  }

  get unreadAlertsCount(): number {
    return this.alerts().filter((a) => !a.isRead).length;
  }
}