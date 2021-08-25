# python-docker-locker
Dockerized python encryption &amp; decryption 

## Step 1

docker build -t python-locker .

## Step 2

Before running the below docker command, make sure to replace '/home/playground/Bloom/docker-locker' with the path of the directory where you want to have the decrypted files

docker run --name lockitup -v /home/playground/Bloom/docker-locker:/usr/src/app -ti python-locker

## Step 3

Enter name of document to be encrypted such as -> 'document.txt' OR 'raze.png'

## Step 4

Enter name of document to be decrypted such as -> 'encrypted_document.txt' OR 'encrypted_raze.png'

## Step 5

Check Out the encrypted and decrypted files.
