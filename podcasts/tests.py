from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Episode


class PodcastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title = "Ecossistema Python",
            description = "Hoje o papo é sobre Python!",
            publication_date = timezone.now(),
            link = "https://www.hipsters.tech/ecossistema-python-hipsters-ponto-tech-387",
            image = "https://i0.wp.com/www.hipsters.tech/wp-content/uploads/2023/12/Hipsters-Ponto-Tech-387-1200x628-1.png?resize=1024%2C536&ssl=1",
            podcast_name = "Hispters.Tech",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Hoje o papo é sobre Python!")
        self.assertEqual(self.episode.link, "https://www.hipsters.tech/ecossistema-python-hipsters-ponto-tech-387")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )
    
    def test_episode_str_representation(self):
        self.assertEqual(str(self.episode), "Hispters.Tech: Ecossistema Python")

    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed("homepage.html")
    
    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "Hispters.Tech")