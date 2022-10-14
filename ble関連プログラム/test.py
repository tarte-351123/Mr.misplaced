import requests
import json
import sys
import pprint



# WEB_HOOK_URLは下準備で発行したURLを設定しください
WEB_HOOK_URL = "https://hooks.slack.com/services/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"

requests.post(WEB_HOOK_URL, data=json.dumps({
    "text" : "財布を置き忘れていませんか？",
}))