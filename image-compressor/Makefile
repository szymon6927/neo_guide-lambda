update-deps:
	pip install pip-tools
	pip-compile --generate-hashes --allow-unsafe src/dev.in --output-file src/dev.txt
	pip-compile --generate-hashes --allow-unsafe src/requirements.in --output-file src/requirements.txt

format:
	black src/ --skip-string-normalization

run-tests:
	cd src/ && python -m pytest tests/ -v -s

sam-build:
	sam build

sam-local-event:
	sam local invoke --event events/event.json

sam-package:
	sam package --output-template-file packaged.yaml --s3-bucket neo-guide-lambda --profile szymon-private

sam-deploy:
	sam deploy --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name image-compressor --profile szymon-private --debug --region eu-central-1
