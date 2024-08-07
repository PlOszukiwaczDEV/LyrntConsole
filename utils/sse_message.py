import requests
from requests_sse import EventSource, InvalidStatusCodeError, InvalidContentTypeError

while True:
    with EventSource("https://lyntr.com/api/sse", timeout=30) as event_source:
        try:
            for event in event_source:
                print(event)
        except InvalidStatusCodeError:
            pass
        except InvalidContentTypeError:
            pass
        except requests.RequestException:
            pass
        except KeyboardInterrupt:
            break