import twitter
import textblob


def main():
    consumer_key = 'YA7o8rljz2lr2lT6x0Pqm9GFJ'
    consumer_secret = 'Jju95zsOX05QPTQTFQi07sdF8zft4zgULYaZMe5rhrAAM3b3bo'
    access_token = '582758531-0ja8Agj3pUI2zOZIxVkDku3CiA7Ke05GygUcZTtG'
    access_secret = '2rPsbe44O9WHGzQ50wLJ3XII1m3gtFfcQ22IjXaGWanEY'
    api = twitter.Api(consumer_key=consumer_key,
                            consumer_secret=consumer_secret,
                          access_token_key=access_token,
                          access_token_secret=access_secret)
    print(api.GetTrendsCurrent())


main()
