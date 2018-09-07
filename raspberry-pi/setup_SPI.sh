USERMS="Ufarm"
echo "${USERMS} : Installing python in case is not already there"
sudo apt-get install python-dev python-dev -y
echo "${USERMS} : Downloading library to perform SPI communication"
wget https://github.com/Gadgetoid/py-spidev/archive/master.zip
echo "${USERMS} : Unziping the library"
unzip master.zip
echo "${USERMS} : Deleting reduntant zip folder"
rm master.zip
echo "${USERMS} : Setting up the library (cd py-spidev-master ; sudo python3 setup.py install) "
cd py-spidev-master
sudo python setup.py install
sudo python3 setup.py install
cd ..
mkdir NRF24L01
cd NRF24L01
git clone https://github.com/BLavery/lib_nrf24
cd lib_nrf24
cp lib_nrf24.py ..

