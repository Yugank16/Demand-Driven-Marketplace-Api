from channels import Group
from apps.bids.models import Bid
from apps.items.models import Item
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Min
from channels.asgi import get_channel_layer
import json

@receiver([post_save, post_delete], sender=Bid)
def updateBid(sender, instance, **kwargs):
    min_price = Bid.objects.filter(item=instance.item).aggregate(min_bid_price=Min('bid_price'))
    min_price = min_price["min_bid_price"]
    item = Item.objects.get(pk=instance.item.id)
    message = {
        "min_price": min_price,
    }
    Group("item-{}".format(instance.item.id)).send({"text": json.dumps(message)})
    item.min_bid_price = min_price
    item.save()

    