import yaml

yml={'member':['name:Taro Yamada address:Hokkaido',
 'name:Ichiro Tanaka address:Tokyo', 'name:Jiro Sato address:Okinawa']}

with open('output.yaml','w') as file:
    yaml.dump(yml,file,default_flow_style=False)
