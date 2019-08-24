from django.test import TestCase

# Create your tests here.

from entities.models import Recording


class testRecording(TestCase):
    def testFetch(self):
        rec = Recording(id="833f00e1-781f-4edd-90e4-e52712618862")
        status = rec.fetch()
        self.assertEqual(status, 200)
        self.assertEqual(rec.title, "Get Lucky")
        self.assertEqual(
            rec.artistCredit, "Daft Punk feat. Pharrell Williams & Nile Rodgers"
        )
