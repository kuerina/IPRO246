g++ -Wall -Ofast -mfpu=vfp -mfloat-abi=hard -march=armv6zk -mtune=arm1176jzf-s -L../librf24/ -lrf24 $1 -o pi_receiver
