import unittest


SERVER = "server A"
currency = "COP"


class AllAssertsTests(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(1, 1)
        self.assertEqual("python", "python")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("Text")

    def test_assert_in(self):
        self.assertIn(10, [1, 2, 3, 10])
        self.assertIn("python", "python is easy")
        self.assertNotIn(10, [1, 2, 3, 4])

    def test_assert_discts(self):
        self.assertDictEqual(
            {"name": "John", "lastname": "Martinez"},
            {"name": "John", "lastname": "Martinez"},
        )

        self.assertSetEqual({1, 2, 3}, {3, 2, 1})

    @unittest.skip("Trabajo en progreso, sera habilita nuevamente")
    def test_skip(self):
        self.assertEqual("python", "js")

    @unittest.skipIf(SERVER == "server A", "Skip because is server A")
    def test_skip_if(self):
        self.assertEqual("python", "js")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual("python", "js")

    @unittest.skipUnless(currency == "USD", "Skip because currency is not USD")
    def test_skip_unless(self):
        self.assertEqual("COP", "USD")
