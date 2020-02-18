# docker-recordurbate

original project: https://github.com/oliverjrose99/Recordurbate. I just changed some things so it would run nice in a docker container.

## How to use
### docker-compose
Download docker-compose if you dont have that already
````bash
pip install docker-compose
````
Download the repo
````bash
git clone https://github.com/LootScooper/docker-recordurbate.git
cd docker-recordurbate
````
Then you edit the docker-compose.yml with an editor of your choice. And change " - /srv/sto1/recordubate:/videos" on line 9. You need to change "/srv/sto1/recordubate" to your video path.
Run!!
````bash
docker-compose up
````
Or if you want to run your container detached (In the background)
````bash
docker-compose up -d
````
https://docs.docker.com/compose/
### docker
````bash
git clone https://github.com/LootScooper/docker-recordurbate.git
cd docker-recordurbate/recordurbate
docker build . -t recordurbate
docker start -d --restart unless-stopped -v your-config-folder:/data -v my-video-folder:/videos recordurbate
````
Make sure you copy config.json and youtube-dl.config to your config folder.
### Example config
```json
{
  "youtube-dl_cmd": "youtube-dl",
  "auto_reload_config": true,
  "rate_limit": true,
  "rate_limit_time": 5,
  "streamers": ["streamer1", "streamer2", "streamer3"]
}
```
```json
{
  "youtube-dl_cmd": "youtube-dl",
  "auto_reload_config": true,
  "rate_limit": true,
  "rate_limit_time": 5,
  "streamers": ["streamer1"]
}
```

## Todo
- [ ] support environment variables 
