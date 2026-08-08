from datetime import date

from django.test import TestCase

from animals.models import Animal
from .models import Reproduction, Naissance


class ReproductionTest(TestCase):

    def setUp(self):

        self.mere = Animal.objects.create(
            numero_identification="V001",
            espece="BOVIN",
            race="Holstein",
            sexe="F"
        )


    def test_creation_reproduction(self):

        reproduction = Reproduction.objects.create(
            mere=self.mere,
            date_insemination=date(2026,1,1)
        )


        self.assertIsNotNone(
            reproduction.date_misebas_prevue
        )


    def test_creation_naissance(self):

        reproduction = Reproduction.objects.create(
            mere=self.mere,
            date_insemination=date(2026,1,1)
        )


        enfant = Animal.objects.create(
            numero_identification="V002",
            espece="BOVIN",
            race="Holstein",
            sexe="M"
        )


        naissance = Naissance.objects.create(
            reproduction=reproduction,
            animal_enfant=enfant,
            date_naissance=date(2026,10,10)
        )


        self.assertEqual(
            naissance.animal_enfant,
            enfant
        )