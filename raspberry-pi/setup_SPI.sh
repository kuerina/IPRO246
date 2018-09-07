USERMS="Ufarm"
echo "${USERMS} : Installing python in case is not already there"
sudo apt-get install python-dev python-dev -y
echo "${USERMS} : Downloading library to perform SPI communication"
wget https://github.com/Gadgetoid/py-spidev/archive/master.zip
echo "${USERMS} : Unziping the library"
unzip master.zip
echo "${USERMS} : Deleting reduntant zip folder"
rm master.zip
