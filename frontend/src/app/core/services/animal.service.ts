import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Animal } from '../../shared/models/animal.model';

@Injectable({ providedIn: 'root' })
export class AnimalService {
  private readonly baseUrl = `${environment.apiUrl}/animals/`;

  constructor(private readonly http: HttpClient) {}

  getAll(): Observable<Animal[]> {
    return this.http.get<Animal[]>(this.baseUrl);
  }

  getById(id: number): Observable<Animal> {
    return this.http.get<Animal>(`${this.baseUrl}${id}/`);
  }

  create(animal: Partial<Animal>): Observable<Animal> {
    return this.http.post<Animal>(this.baseUrl, animal);
  }

  update(id: number, animal: Partial<Animal>): Observable<Animal> {
    return this.http.patch<Animal>(`${this.baseUrl}${id}/`, animal);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}${id}/`);
  }
}