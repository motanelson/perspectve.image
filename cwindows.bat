python3 -m ppci cc -c %1 -o %1.o  --machine x86_64 
python3 -m ppci ld --entry main %1.o -o %1.elf 
