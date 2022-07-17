# NOTE: Generated By HttpRunner v3.1.6
# FROM: har/mubudemo.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubudemo(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/home")
            .get("https://mubu.com/home")
            .with_headers(
                **{
                    "cache-control": "max-age=0",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"macOS"',
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1657468223",
                    "SLARDAR_WEB_ID": "70a12b35-2c3a-41b3-a610-7b59dca4b9f1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1657468240",
                    "data_unique_id": "88fa8d79-f947-4206-92ad-5cc38f630c6f",
                    "language": "en-US",
                    "country": "US",
                    "SESSION": "3a7d05a6-95b7-4984-a331-364f3bb4bf63",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2Fsettings%23",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiNDg3MjA4IiwibG9naW5UeXBlIjoibW9iaWxlIiwiZXhwIjoxNjYwNDk1NDk3LCJpYXQiOjE2NTc5MDM0OTd9.GAiXg_pM4l5ob9pNsN2u18iNj0YJCCG-yZ_s2JvVCFhNZsIoDS7LLbRmKMiM6gSROffalQ58PIlYh6RAm_laWA",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/app")
            .get("https://mubu.com/app")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"macOS"',
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/home",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1657468223",
                    "SLARDAR_WEB_ID": "70a12b35-2c3a-41b3-a610-7b59dca4b9f1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1657468240",
                    "data_unique_id": "88fa8d79-f947-4206-92ad-5cc38f630c6f",
                    "language": "en-US",
                    "country": "US",
                    "SESSION": "3a7d05a6-95b7-4984-a331-364f3bb4bf63",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2Fsettings%23",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiNDg3MjA4IiwibG9naW5UeXBlIjoibW9iaWxlIiwiZXhwIjoxNjYwNDk1NDk3LCJpYXQiOjE2NTc5MDM0OTd9.GAiXg_pM4l5ob9pNsN2u18iNj0YJCCG-yZ_s2JvVCFhNZsIoDS7LLbRmKMiM6gSROffalQ58PIlYh6RAm_laWA",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseMubudemo().test_start()