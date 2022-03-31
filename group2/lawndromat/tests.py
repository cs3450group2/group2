from urllib import request
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
        


class registerTestCase(TestCase):
    def test_Request(self):
        request = Request.objects.create(requestZip=84341,
            customerID= 1,
            date="2022-03-12",
            timeOfDay="morning",
            workerID=1,
            complete=False,
            feedBack="yes",
            thumbsUp=False,
            cost=10.0,
            type="lawn")
        self.assertEqual(request.timeOfDay, "morning")
        self.assertEqual(request.complete, False)
        self.assertEqual(request.feedBack, "yes")
        self.assertEqual(request.cost, 10.0)