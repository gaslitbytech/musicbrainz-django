import datetime

from django.db import models
from django.utils import timezone

"""
<artist id="86de477a-4c88-44f4-b0e3-9ef2efa954dc" type="Person" type-id="b6e035f4-3ce9-331c-97df-83397230b0df" ns2:score="100">
    <name>Tom Redwood</name>
    <sort-name>Redwood, Tom</sort-name>
    <gender>male</gender>
    <area id="b4e9352c-8edf-4911-8fa3-e852afa30501" type="City" type-id="6fd8f29a-3d0a-32fc-980d-ea697b69da78">
        <name>Melbourne</name>
        <sort-name>Melbourne</sort-name>
        <life-span>
            <ended>false</ended>
        </life-span>
    </area>
    <disambiguation>Australian Singer Songwriter>
    <begin-area id="7dc47ab9-c7ff-4282-97e0-bd53db80ff9d" type="City" type-id="6fd8f29a-3d0a-32fc-980d-ea697b69da78">
        <name>Adelaide</name>
        <sort-name>Adelaide</sort-name>
        <life-span>
            <ended>false</ended>
        </life-span>
    </begin-area>
    <life-span>
        <ended>false</ended>
    </life-span>
</artist>
"""
class Artist(models.Model):
    name = models.TextField()
    disambiguation = models.TextField()
