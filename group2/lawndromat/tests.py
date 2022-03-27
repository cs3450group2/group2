from django.test import TestCase
from .models import UserProfile, Request
from django.contrib.auth.models import User
        
        
class ProfileTestCase(TestCase):
    def test_profile(self):
        user1 = User.objects.create_user(username="test@test.com",
                                         email="test@test.com",
                                         password="password")
        UserProfile.objects.create(user=user1,
                              userName = "Worker",
                              userZipCode = "12345",
                              userAddress = "100 Test Ave",
                              userType = "worker",
                              money = 0)
        user2 = User.objects.create_user(username="test2@test.com",
                                         email="test2@test.com",
                                         password="password")
        UserProfile.objects.create(user=user2,
                              userName = "Customer",
                              userZipCode = "12345",
                              userAddress = "100 Test Ave",
                              userType = "customer",
                              money = 0)
    
        self.assertEqual(user1.userprofile.userName, "Worker")
        self.assertEqual(user2.userprofile.userName, "Customer")