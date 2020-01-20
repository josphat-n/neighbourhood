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
      
   # Testing Save Method
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
      