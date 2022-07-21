
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubuLogin(HttpRunner):


    config = Config("mubu login").verify(False)\
        .base_url("https://api2.mubu.com/")\
        .variables(**{"host":"mubu.com"})\
        .variables(**{"phone": "18976231206", "password": "369874125"})\

    teststeps = [
        Step(
            RunRequest("/v3/api/user/phone_login")
            .post("/v3/api/user/phone_login")
            .with_headers(
                **{
                    "content-length": "63",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "88fa8d79-f947-4206-92ad-5cc38f630c6f",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "",
                    "x-request-id": "f3babbb3-056e-4e69-9dcb-638c40d5e311",
                    "sec-ch-ua-platform": '"macOS"',
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json(
                {"phone": "$phone", "password": "$password", "callbackType": 0}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.data.id", 487208)
        ),
    ]

if __name__ == "__main__":
    TestCaseMubuLogin().test_start()