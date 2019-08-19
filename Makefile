all: serve

init:
	createdb dataproviderdb
	psql --quiet --file=seed.sql dataproviderdb

	aws dynamodb create-table \
		--table-name Templates \
		--attribute-definitions AttributeName=Language,AttributeType=S \
		--key-schema AttributeName=Language,KeyType=HASH \
		--provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=5
	aws dynamodb wait table-exists --table-name Templates
	aws dynamodb put-item --table-name Templates --item '{"Language": {"S": "en"}, "Template": {"S": "Yo, {}!"}}'
	aws dynamodb put-item --table-name Templates --item '{"Language": {"S": "ja"}, "Template": {"S": "おい、{}！"}}'

serve:
	pip3 install --quiet --requirement requirements.txt
	pip3 install --quiet --editable .
	python3 dataproviderexample/onprem/app.py

clean:
	-dropdb dataproviderdb
	-aws dynamodb delete-table --table-name Templates
	-aws dynamodb wait table-not-exists --table-name Templates

.PHONY: all init serve clean
