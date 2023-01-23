from .test_setup import TestSetUp

class TestViews(TestSetUp):

    def test_user_cannot_register_without_credentials(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register(self):
        user_data = {
            "email":"email@example.com",
            "password1":"P@55w0rd",
            "password2":"P@55w0rd"
        }
        res = self.client.post(self.register_url, 
            user_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_user_not_permitted_without_verification(self):
        res = self.client.post(self.login_url, 
            self.user_data, format="json")
        self.assertEqual(res.status_code, 401)