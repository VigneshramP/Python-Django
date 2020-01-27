from django.test import TestCase
from models import *

# Create your tests here.


class OverallDefectsTestCase(TestCase):
    def setUp(self):
        OverallDefects.objects.create(id = '123', part_defect = '2', observations = "Painting Not Properly")
        OverallDefects.objects.create(id = 'mea123', part_defect = '1', observations = "Gear Teeth has been Broken")

    def test_overall_defects(self):
        defect1 = OverallDefects.objects.create(id = '123', part_defect = '2', observations = "Painting Not Properly")
        defect2 =  OverallDefects.objects.create(id = 'mea123', part_defect = '1', observations = "Gear Teeth has been Broken")
        
# Part Defects Field Test Cases
	self.assertEqual(defect1.part_defect(),  "2")
        self.assertEqual(defect2.part_defect(), '1')
	self.assertNotEqual(defect1.part_defect(),  "1")
        self.assertNotEqual(defect2.part_defect(), '3')
	self.assertTrue(defect1.part_defect(),  "2")
        self.assertTrue(defect2.part_defect(), '1')
	self.assertFalse(defect1.part_defect(),  "2")
        self.assertFalse(defect2.part_defect(), '1')
	
# Observations Field Test Cases
	self.assertEqual(defect1.observations(),  "Painting Not Properly")
        self.assertEqual(defect2.observations(), "Gear Teeth has been Broken")
	self.assertNotEqual(defect1.observations(),  "Paint")
        self.assertNotEqual(defect2.observations(), 'gear')
	self.assertTrue(defect1.observations(),  "Painting Not Properly")
        self.assertTrue(defect2.observations(), "Gear Teeth has been Broken")
	self.assertFalse(defect1.observations(),  "Paint")
        self.assertFalse(defect2.observations(), 'Gear')
