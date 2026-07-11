export type AnimalSex = 'male' | 'female';
export type AnimalStatus = 'active' | 'sold' | 'deceased' | 'quarantine';

export interface Animal {
  id: number;
  identifier: string;
  species: string;
  breed: string;
  sex: AnimalSex;
  birthDate: string;
  status: AnimalStatus;
  weightKg?: number;
  notes?: string;
  createdAt: string;
  updatedAt: string;
}