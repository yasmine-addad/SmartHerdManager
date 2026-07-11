import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { User } from '../../shared/models/user.model';

@Injectable({ providedIn: 'root' })
export class UserService {
  private readonly baseUrl = `${environment.apiUrl}/users/`;

  constructor(private readonly http: HttpClient) {}

  getAll(): Observable<User[]> {
    return this.http.get<User[]>(this.baseUrl);
  }

  updateRole(id: number, role: User['role']): Observable<User> {
    return this.http.patch<User>(`${this.baseUrl}${id}/`, { role });
  }

  toggleActive(id: number, isActive: boolean): Observable<User> {
    return this.http.patch<User>(`${this.baseUrl}${id}/`, { isActive });
  }
}