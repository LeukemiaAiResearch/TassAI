######################################################################################################
#
# Organization:  Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss
# Project:       UP2 NCS1 Facial Recognition USB Security System
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
#

# Title:         TassAI Class
# Description:   TassAI NCS1 USB Camera Security System class.
# License:       MIT License
# Last Modified: 2020-09-28
#
######################################################################################################

import cv2

from Classes.Helpers import Helpers
from Classes.OpenCV import OpenCV
from Classes.NCS1 import NCS1

class TassAI():
	""" TassAI Class

	TassAI HIAS NCS1 USB Camera Security System class.
	"""

	def __init__(self):
		""" Initializes the class. """

		self.Helpers = Helpers("TassAI")

		self.Helpers.logger.info("TassAI class initialized.")

	def cv(self):
		""" Configures OpenCV. """

		self.font = cv2.FONT_HERSHEY_SIMPLEX
		self.color = (255,255,255)
		self.fontScale  = 1
		self.lineType = 1

	def connect(self):
		""" Connects to the USB camera. """

		self.camera = OpenCV(self.Helpers.confs["Camera"]["Id"])

	def ncs(self):
		""" Configures NCS1. """

		self.NCS1 = NCS1()

		self.known = self.Helpers.confs["Classifier"]["Known"]
		self.test = self.Helpers.confs["Classifier"]["Test"]

		self.detector = self.NCS1.Detector
		self.predictor = self.NCS1.Predictor

		self.Helpers.logger.info("NCS1 configured.")
