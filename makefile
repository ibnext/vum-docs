YQ := $(shell command -v yq 2> /dev/null)

check-dependencies:
	@if [[ "$(YQ)" == "" ]]; then\
		echo "Error: yq not found. Please install yq:"; \
		echo "  macOS:   brew install yq"; \
		echo "  Ubuntu:  apt-get install yq"; \
		echo "  Others:  https://github.com/mikefarah/yq#install"; \
		exit 1; \
	fi

tojson: check-dependencies
	@for file in OAS_Contracten/*.yaml; do \
		echo "Converting $$file"; \
		json_file=`echo $$file | sed "s/.yaml/.json/"`; \
		yq -o=json "$$file" > "$$json_file"; \
		echo "Converted $$file to $$json_file"; \
	done

clean:
	@echo "No cleanup needed for yq implementation"

