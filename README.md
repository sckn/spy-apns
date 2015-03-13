# spy-apns
This library send push notification with apns.

#Example
```python
import spyapns
payload = spyapns.init_payload('hello world')
token = "<token>"
cert  = "/full/path/cert.pem"
spyapns.send(cert=cert, payload=payload, token=token)
```
```bash
#!/bin/bash
# script.sh "hello world" "cert.pem" "really_large_token"
python spyapns.py -a "$1" -c $2 -d $3
```
