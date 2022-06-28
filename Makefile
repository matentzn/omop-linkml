RUN=poetry run

model/:
	mkdir -p $@

all: target/persons.ttl

persons.ttl:
	$(RUN) linkml-convert -t rdf -s omop.yaml -S person_list -C Person person.tsv

omop.py: omop.yaml | model/
	$(RUN) gen-project -d model $< && cp model/omop.py $@
