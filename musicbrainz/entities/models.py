import datetime
import uuid

from django.db import models
from django.utils import timezone

"""
<artist-list>
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
    <artist id="be136e58-ccf5-47f0-a000-6e8d7eb3bae0" type="Group" ext:score="61">
      <name>The Color Fred</name>
      <sort-name>Color Fred, The</sort-name>
      <country>US</country>
      <area id="489ce91b-6658-3307-9877-795b68554c98">
        <name>United States</name>
        <sort-name>United States</sort-name>
      </area>
      <life-span>
        <begin>2003</begin>
        <ended>false</ended>
      </life-span>
    </artist>
        <artist id="4a024fd4-305e-4fea-9d3f-4ec858766e6e" type="Group" ext:score="100">
      <name>Fred</name>
      <sort-name>Fred</sort-name>
      <country>US</country>
      <area id="489ce91b-6658-3307-9877-795b68554c98">
        <name>United States</name>
        <sort-name>United States</sort-name>
      </area>
      <disambiguation>US comic barbershop quartet</disambiguation>
      <life-span>
        <ended>false</ended>
      </life-span>
        <artist id="05cfb5c7-0152-41f4-a9c9-622e8f710dfa" type="Group" ext:score="51">
      <name>John Fred & His Playboy Band</name>
      <sort-name>Fred, John & His Playboy Band</sort-name>
      <country>US</country>
      <area id="489ce91b-6658-3307-9877-795b68554c98">
        <name>United States</name>
        <sort-name>United States</sort-name>
      </area>
      <begin-area id="34f02dc4-3173-4c68-86d1-c82504759342">
        <name>Baton Rouge</name>
        <sort-name>Baton Rouge</sort-name>
      </begin-area>
      <life-span>
        <begin>1956</begin>
        <end>1969</end>
        <ended>true</ended>
      </life-span>
      <alias-list>
        <alias sort-name="John Fred">John Fred</alias>
        <alias sort-name="John Fred and His Playboyband">John Fred and His Playboyband</alias>
        <alias sort-name="John Fred and His Play Boy Band">John Fred and His Play Boy Band</alias>
        <alias sort-name="John Fred And His Playboy Band">John Fred And His Playboy Band</alias>
        <alias sort-name="John Fred and His Playboys">John Fred and His Playboys</alias>
        <alias sort-name="John Fred and the Play Boy Band">John Fred and the Play Boy Band</alias>
        <alias sort-name="John Fred and the Playboys">John Fred and the Playboys</alias>
        <alias sort-name="John Fred & His Playboyband">John Fred & His Playboyband</alias>
        <alias sort-name="John Fred & His Playboys">John Fred & His Playboys</alias>
        <alias sort-name="John Fred & Hiss Playboy Band">John Fred & Hiss Playboy Band</alias>
        <alias sort-name="John Fred & Playboyband">John Fred & Playboyband</alias>
        <alias sort-name="John Fred & Playboy Band">John Fred & Playboy Band</alias>
        <alias sort-name="John Fred & the Play Boy Band">John Fred & the Play Boy Band</alias>
        <alias sort-name="John Fred & The Playboyband">John Fred & The Playboyband</alias>
        <alias sort-name="John Fred & The Playboy Band">John Fred & The Playboy Band</alias>
        <alias sort-name="John Fred & The Playboys">John Fred & The Playboys</alias>
      </alias-list>
    </artist>
    </artist-list>
"""
class Artist(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.TextField()
    disambiguation = models.TextField()

    # TODO Add fields ignored from above

class ArtistSearch(models.Model):
    alias = models.TextField()  #	an alias attached to the artist
    area = models.TextField()  #	the artist's main associated area
    arid = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )  #	the artist's MBID
    artist = models.TextField()  #	the artist's name (without accented characters)
    artistaccent = models.TextField()  #	the artist's name (with accented characters)
    begin = models.TextField()  #	the artist's begin date
    beginarea = models.TextField()  #	the artist's begin area
    comment = models.TextField()  #	the artist's disambiguation comment
    country = models.TextField()  #	the 2-letter code (ISO 3166-1 alpha-2) for the artist's main associated country, or “unknown”
    end = models.TextField()  #	the artist's end date
    endarea = models.TextField()  #	the artist's end area
    ended = models.TextField()  #	a flag indicating whether or not the artist has ended
    gender = models.TextField()  #	the artist's gender (“male”, “female”, or “other”)
    ipi = models.TextField()  #	an IPI code associated with the artist
    sortname = models.TextField()  #	the artist's sort name
    tag = models.TextField()  #	a tag attached to the artist
    _type = models.TextField()  #	the artist's type (“person”, “group”, ...)
