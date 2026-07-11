export type AlertSeverity = 'info' | 'warning' | 'critical';
export type AlertType = 'vaccine' | 'birth' | 'appointment' | 'health' | 'other';

export interface Alert {
  id: number;
  type: AlertType;
  severity: AlertSeverity;
  message: string;
  animalId?: number;
  dueDate: string;
  isRead: boolean;
  createdAt: string;
}