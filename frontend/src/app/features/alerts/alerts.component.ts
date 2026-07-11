import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AlertService } from '../../core/services/alert.service';
import { Alert } from '../../shared/models/alert.model';

@Component({
  selector: 'app-alerts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './alerts.component.html',
  styleUrl: './alerts.component.css',
})
export class AlertsComponent implements OnInit {
  readonly alerts = signal<Alert[]>([]);
  readonly isLoading = signal(true);

  constructor(private readonly alertService: AlertService) {}

  ngOnInit(): void {
    this.alertService.getAll().subscribe((alerts) => {
      this.alerts.set(alerts);
      this.isLoading.set(false);
    });
  }

  markAsRead(alert: Alert): void {
    this.alertService.markAsRead(alert.id).subscribe((updated) => {
      this.alerts.update((list) => list.map((a) => (a.id === updated.id ? updated : a)));
    });
  }
}