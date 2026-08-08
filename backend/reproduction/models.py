from datetime import timedelta

from django.db import models

from animals.models import Animal


class Reproduction(models.Model):
    

    mere = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name="reproductions"
    )

    date_insemination = models.DateField()

    date_misebas_prevue = models.DateField(
        blank=True,
        null=True
    )

    date_misebas_reelle = models.DateField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-date_insemination"]
        verbose_name = "Reproduction"
        verbose_name_plural = "Reproductions"

    def save(self, *args, **kwargs):
        
        if self.date_insemination and not self.date_misebas_prevue:
            self.date_misebas_prevue = (
                self.date_insemination + timedelta(days=283)
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.mere.numero_identification} - "
            f"{self.date_insemination}"
        )


class Naissance(models.Model):
    """
    Représente la naissance d'un animal.
    """

    reproduction = models.ForeignKey(
        Reproduction,
        on_delete=models.CASCADE,
        related_name="naissances"
    )

    animal_enfant = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name="naissances"
    )

    date_naissance = models.DateField()

    class Meta:
        ordering = ["-date_naissance"]
        verbose_name = "Naissance"
        verbose_name_plural = "Naissances"

    def __str__(self):
        return (
            f"{self.animal_enfant.numero_identification} "
            f"({self.date_naissance})"
        )
