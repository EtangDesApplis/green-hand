# daemons

```
docker build -t etangdesapplis/gh-daemons daemons/
```

# api

To build image:
```
docker build -t etangdesapplis/gh-daemons api/
```
To test:
```
curl https://chefphan.com/gh-api/ -d '{"email":"nguyen.ensma5@gmail.com","name":"Quan","info":"","seeds":[{"variety":"rose","seedingOutdoor":["3"],"seedingIndoor":["4"],"harvest":["6"],"exposition":"","timeToHarvest":"50"}]}' -H 'Content-Type: application/json'
```