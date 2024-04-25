# Australian addresses

addresses uniquely identified by the combination of street, suburb, and region.

download data from:

https://www.kaggle.com/datasets/sreekanthvasireddy/australia-address

## prep

```shell
pip install uv

uv venv

source .venv/bin/activate

uv pip install -r requirements.in
```

## input

`Australia Address.csv`

```csv
,unit_type,number,street,suburb,region,postcode,lat,lon
0,UNIT 39,60,JOHN GORTON DRIVE,COOMBS,ACT,2611.0,-35.321,149.04
```

## run

```shell
python main.py
```

## output

`output.csv`

```csv
street,suburb,region,postcode
JOHN GORTON DRIVE,COOMBS,ACT,2611
```
