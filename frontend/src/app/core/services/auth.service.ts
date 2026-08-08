import { Injectable, signal, computed } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { environment } from '../../../environments/environment';
import { AuthCredentials, AuthResponse, User } from '../../shared/models/user.model';

const ACCESS_TOKEN_KEY = 'shm_access_token';
const REFRESH_TOKEN_KEY = 'shm_refresh_token';
const USER_KEY = 'shm_current_user';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly currentUserSignal = signal<User | null>(this.readStoredUser());

  readonly currentUser = computed(() => this.currentUserSignal());
  readonly isAuthenticated = computed(() => !!this.currentUserSignal());

  constructor(private readonly http: HttpClient) {}

  login(credentials: AuthCredentials): Observable<AuthResponse> {
    return this.http
      .post<AuthResponse>(`${environment.apiUrl}/login/`, credentials)
      .pipe(tap((response) => this.persistSession(response)));
  }

  register(payload: AuthCredentials & { firstName: string; lastName: string }): Observable<AuthResponse> {
    return this.http
      .post<AuthResponse>(`${environment.apiUrl}/register/`, payload)
      .pipe(tap((response) => this.persistSession(response)));
  }

  logout(): void {
    localStorage.removeItem(ACCESS_TOKEN_KEY);
    localStorage.removeItem(REFRESH_TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
    this.currentUserSignal.set(null);
  }

  getAccessToken(): string | null {
    return localStorage.getItem(ACCESS_TOKEN_KEY);
  }

  private persistSession(response: AuthResponse): void {
    localStorage.setItem(ACCESS_TOKEN_KEY, response.access);
    localStorage.setItem(REFRESH_TOKEN_KEY, response.refresh);
    localStorage.setItem(USER_KEY, JSON.stringify(response.user));
    this.currentUserSignal.set(response.user);
  }

  private readStoredUser(): User | null {
    const raw = localStorage.getItem(USER_KEY);
    return raw ? (JSON.parse(raw) as User) : null;
  }

  forgotPassword(email: string) {
  return this.http.post(
    `${environment.apiUrl}/forgot-password/`,
    { email }
  );
}

   resetPassword(
    uid: string,
    token: string,
    password: string 
  ) 
    {
      return this.http.post(
        `${environment.apiUrl}/reset-password/`,
        {
          uid,
          token,
          password
        }
      );
    }
}