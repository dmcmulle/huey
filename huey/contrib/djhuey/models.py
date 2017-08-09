from django.db import models
import uuid


class DJHueyAcksLate(models.Model):
    _STATUS_QUEUED_ = "_QUEUED_"
    _STATUS_IN_PROGRESS_ = "_IN_PROGRESS_"
    _STATUS_DONE_ = "_DONE_"

    _STATUS_CHOICES = (
        (_STATUS_QUEUED_, "Queued"),
        (_STATUS_IN_PROGRESS_, "In Progress"),
        (_STATUS_DONE_, "Done")
    )

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)

    status = models.CharField(
        max_length=32,
        verbose_name="Status of the report",
        choices=_STATUS_CHOICES,
        default=_STATUS_IN_PROGRESS_
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)