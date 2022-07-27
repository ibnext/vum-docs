YAML2JSON := $(shell command -v yaml2json 2> /dev/null)


tojson: OAS_Contracten/*.yaml
	@if [[ "$(YAML2JSON)" == "" ]]; then\
		echo 'installing yaml2json'; \
		go install github.com/mbrukman/yaml2json/cmd/yaml2json@latest; \
	fi
	for file in $^ ; do \
		echo "Generating for $$file"; \
		echo $$file| sed "s/.yaml/.json/"; \
		yaml2json $$file > `echo $$file| sed "s/.yaml/.json/"`; \
	done

