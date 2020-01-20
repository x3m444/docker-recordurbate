# docker-recordurbate
## How to use
- put streamer or streamers in config.json
- change download location in docker-compose.yml
- docker-compose up
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
