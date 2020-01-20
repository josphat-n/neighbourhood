from django.test import TestCase
from .models import Hood, Business, Admin

# Create your tests here.
class HoodTestClass(TestCase):
   # Setup Method
   def setUp(self):
      self.hood_one=Hood(name= 'Muthaiga', admin_id=1, location = 'Kiambu', occupants_count = 1)
   
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.hood_one,Hood))     
      
   # Testing create Method
   def test_create_method(self):
      self.hood_one.create_hood()
      hood1 = Hood.objects.all()
      self.assertTrue(len(hood1) > 0)    
      
   # Teardown Method
   def tearDown(self):
      Hood.objects.all().delete()           
   
   #Delete Method   
   def test_delete(self):
      self.hood_one.create_hood()
      self.hood_one.delete_hood()
      hood1 = Hood.objects.all()
      self.assertTrue(len(hood1)<1)    
      
      
class BusinessTestClass(TestCase):
   # Setup Method
   def setUp(self):
      self.business_one=Business(name= 'Awesome_Kinyozi', hood_id=1, biz_email = 'Kinyozi@gmail.com')  
   
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.business_one,Business))  
      
   # Testing Create Method
   def test_create_method(self):
      self.business_one.create_business()
      biz = Business.objects.all()
      self.assertTrue(len(biz) > 0)           
      
      
   # Teardown Method
   def tearDown(self):
      Business.objects.all().delete()           
   
   #Delete Method   
   def test_delete(self):
      self.business_one.create_business()
      self.business_one.delete_business()
      biz = Business.objects.all()
      self.assertTrue(len(biz)<1)       
      