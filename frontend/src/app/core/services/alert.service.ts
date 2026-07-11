import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Alert } from '../../shared/models/alert.model';

@Injectable({ providedIn: 'root' })
export class AlertService {
  private readonly baseUrl = `${environment.apiUrl}/alerts/`;

  constructor(private readonly http: HttpClient) {}

  getAll(): Observable<Alert[]> {
    return this.http.get<Alert[]>(this.baseUrl);
  }

  markAsRead(id: number): Observable<Alert> {
    return this.http.patch<Alert>(`${this.baseUrl}${id}/`, { isRead: true });
  }
}