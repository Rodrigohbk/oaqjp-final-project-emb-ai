from EmotionDetection import emotion_detector

import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test to confirm the expected result "joy"
        case_1 = emotion_detector("I am glad this happened")
        self.assertEqual(case_1.get("dominant_emotion"), "joy")

        # Test to confirm the expected result "anger"
        case_2 = emotion_detector("I am really mad about this")
        self.assertEqual(case_2.get("dominant_emotion"), "anger")

        # Test to confirm the expected result "disgust"
        case_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(case_3.get("dominant_emotion"), "disgust")

        # Test to confirm the expected result "sadness"
        case_4 = emotion_detector("I am so sad about this")
        self.assertEqual(case_4.get("dominant_emotion"), "sadness")

        # Test to confirm the expected result "fear"
        case_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(case_5.get("dominant_emotion"), "fear")


if __name__ == "__main__":
    unittest.main()