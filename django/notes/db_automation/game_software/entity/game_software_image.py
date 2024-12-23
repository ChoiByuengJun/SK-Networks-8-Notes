from django.db import models

from game_software.entity.game_software import GameSoftware


class GameSoftwareImage(models.Model):
    id = models.AutoField(primary_key=True)
    gameSoftware = models.ForeignKey(GameSoftware, on_delete=models.CASCADE, related_name="images")
    image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'game_software_image'
        app_label = 'game_software'

    def __str__(self):
        return f"GameSoftwareImage(id={self.id}, image={self.image})"

    def getImage(self):
        return self.image
