

tojson: OAS_Contracten/*.yaml
	for file in $^ ; do \
		echo "Generating for $$file"; \
		echo $$file| sed "s/.yaml/.json/"; \
		yaml2json $$file > `echo $$file| sed "s/.yaml/.json/"`; \
	done

