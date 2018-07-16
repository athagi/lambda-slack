#!/bin/bash

zip -r upload.zip *

aws lambda update-function-code --function-name slack --zip-file fileb:///Users/hagita/git/slack-python/upload.zip --no-verify-ssl