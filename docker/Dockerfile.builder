FROM gcc:latest

WORKDIR /build

# COPY source_code .

CMD ["g++", "-g", "source_code/mappings.cpp", "-o", "source_code/build_output.exe"]