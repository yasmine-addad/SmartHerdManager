import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnimalService } from '../../core/services/animal.service';
import { Animal } from '../../shared/models/animal.model';

@Component({
  selector: 'app-animals',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './animals.component.html',
  styleUrl: './animals.component.css',
})
export class AnimalsComponent implements OnInit {
  readonly animals = signal<Animal[]>([]);
  readonly isLoading = signal(true);

  constructor(private readonly animalService: AnimalService) {}

  ngOnInit(): void {
    this.animalService.getAll().subscribe((animals) => {
      this.animals.set(animals);
      this.isLoading.set(false);
    });
  }
}