import slackweb
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text="置き忘れしてませんか？")