import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService } from '../../core/services/user.service';
import { User } from '../../shared/models/user.model';

@Component({
  selector: 'app-users',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './users.component.html',
  styleUrl: './users.component.css',
})
export class UsersComponent implements OnInit {
  readonly users = signal<User[]>([]);
  readonly isLoading = signal(true);

  constructor(private readonly userService: UserService) {}

  ngOnInit(): void {
    this.userService.getAll().subscribe((users) => {
      this.users.set(users);
      this.isLoading.set(false);
    });
  }

  toggleActive(user: User): void {
    this.userService.toggleActive(user.id, !user.isActive).subscribe((updated) => {
      this.users.update((list) => list.map((u) => (u.id === updated.id ? updated : u)));
    });
  }
}