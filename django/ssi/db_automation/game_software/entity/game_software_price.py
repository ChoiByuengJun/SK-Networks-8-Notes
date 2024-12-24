from django.db import models

from game_software.entity.game_software import GameSoftware


class GameSoftwarePrice(models.Model):
    id = models.AutoField(primary_key=True)
    gameSoftware = models.ForeignKey(GameSoftware, on_delete=models.CASCADE, related_name="prices")
    price = models.IntegerField()

    class Meta:
        db_table = 'game_software_price'
        app_label = 'game_software'

    def __str__(self):
        return f"GameSoftwarePrice(id={self.id}, price={self.price})"

    def getPrice(self):
        return self.price