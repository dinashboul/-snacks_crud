from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class SnackTest(TestCase):
    def test_snack_list_view(self):
        url=reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snack_list.html")    

    
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username="test", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="TEST", description="description test", purchaser=self.user,
        )


    def test_string (self):
        self.assertEqual(str(self.snack), "TEST")    

    def test_snack_details(self) :
        url= reverse('snack_detail',args="1")
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)  
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_create_view(self):

        data={
                "title": "test",
                "description": "test",
                "purchaser": self.user.id,  

         }
        url = reverse('create_snack')
        response= self.client.post(path=url,data=data,follow=True)
        self.assertRedirects(response,reverse('snack_list'))
    
    
    def test_delete(self):
        url=reverse('delete_snack',args='1')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)