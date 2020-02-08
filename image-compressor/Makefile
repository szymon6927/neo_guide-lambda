update-deps:
	pip install pip-tools
	pip-compile --generate-hashes --allow-unsafe notifications/dev.in --output-file notifications/dev.txt
	pip-compile --generate-hashes --allow-unsafe notifications/requirements.in --output-file notifications/requirements.txt

format:
	black notifications --skip-string-normalization
	isort --apply

run-tests:
	cd notifications/ && python -m pytest tests/ -v -s


sam-build:
	sam build

sam-local-event:
	sam local invoke --event events/event.json

sam-package:
	sam package --output-template-file packaged.yaml --s3-bucket neo-guide-lambda --profile szymon-private

sam-deploy:
	sam deploy --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name image-compressor --profile szymon-private --debug --region eu-central-1
