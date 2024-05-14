from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    sign_up_method = models.CharField(max_length=255, default='Google')


class MapEntity(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    latGroup = models.IntegerField(blank=True, null=True) # used for faster search queries
    lonGroup = models.IntegerField(blank=True, null=True) # used for faster search queries
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='map_entities', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_viewable = models.BooleanField(default=False)  # display on map

    class Meta:
        indexes = [
            models.Index(fields=['latGroup', 'lonGroup']),
        ]

    def save(self, *args, **kwargs):
        self.latGroup = int(self.latitude)
        self.lonGroup = int(self.longitude)
        super(MapEntity, self).save(*args, **kwargs)

    def add_attribute(self, attribute_name, value):
        EntityAttribute.objects.get_or_create(entity=self, attribute_name=attribute_name, value=value)


class EntityAttribute(models.Model):
    entity = models.ForeignKey(MapEntity, on_delete=models.CASCADE, related_name='attributes')
    attribute_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name
