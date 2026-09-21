import json

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")


class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            school="Universitas Indonesia",
            degree="Bachelor's Degree",
            field_of_study="Information System",
            start_year=2025,
        )

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_data_is_displayed(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, self.education.school)
        self.assertContains(response, "Bachelor&#x27;s Degree")
        self.assertContains(response, self.education.field_of_study)
        self.assertContains(response, str(self.education.start_year))

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(
            response,
            "No education information has been added yet."
        )

    def test_create_education(self):
        response = self.client.post(
            reverse("main:create_education"),
            {
                "school": "HIT",
                "degree": "Bachelor's Degree",
                "field_of_study": "Artificial Intelligence",
                "start_year": 2025,
                "end_year": "",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Education.objects.filter(
                school="HIT",
                field_of_study="Artificial Intelligence",
            ).exists()
        )

    def test_update_education(self):
        response = self.client.post(
            reverse(
                "main:edit_education",
                args=[self.education.id],
            ),
            {
                "school": "Harbin Institute of Technology",
                "degree": "Bachelor's Degree",
                "field_of_study": "Artificial Intelligence",
                "start_year": 2025,
                "end_year": "",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.education.refresh_from_db()

        self.assertEqual(
            self.education.school,
            "Harbin Institute of Technology",
        )
        self.assertEqual(
            self.education.field_of_study,
            "Artificial Intelligence",
        )

    def test_delete_education(self):
        education_id = self.education.id

        response = self.client.post(
            reverse(
                "main:delete_education",
                args=[education_id],
            )
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Education.objects.filter(id=education_id).exists()
        )

    def test_education_json(self):
        response = self.client.get(
            reverse("main:get_education_json")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/json",
        )

        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0]["model"],
            "main.education",
        )
        self.assertEqual(
            data[0]["fields"]["school"],
            self.education.school,
        )

    def test_education_search(self):
        Education.objects.create(
            school="Harbin Institute of Technology",
            degree="Bachelor's Degree",
            field_of_study="Artificial Intelligence",
            start_year=2025,
        )

        response = self.client.get(
            reverse("main:show_education"),
            {"school": "Harbin"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Harbin Institute of Technology",
        )
        self.assertNotContains(
            response,
            "Universitas Indonesia",
        )