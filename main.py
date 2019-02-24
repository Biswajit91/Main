from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/Biswajit91/Main')
    ota_updater.download_and_install_update_if_available('Tenda_546FA8', '12345678')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    import time
    from machine import Pin
    led=Pin(2,Pin.OUT)          #create LED object from pin2,Set Pin2 to output

while True:
  led.value(1)              #turn off
  time.sleep(0.5)
  led.value(0)              #turn on
  time.sleep(0.5)

def boot():
    download_and_install_update_if_available()
    start()


boot()
