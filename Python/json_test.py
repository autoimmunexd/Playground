import qbittorrentapi

url = 'http://192.168.1.144:8085/api/v2/torrents/info'

#python -m pip install qbittorrent-api==2022.8.34
#get all torrents with 11 or more seeders and stop seeding them after ratio 1.0
#if a torrent has 13 or less seeders seed indefinately
#ask tracker for more peers (force reannounce)
#add to webui for homelab user stats

info = dict(
    host="127.0.0.1",
    port=5000,
    username="admin",
    password="admin",
)

qbt_client = qbittorrentapi.Client(**info)

for torrent in qbt_client.torrents_info():
    print(f"{torrent.hash[-6:]}:\n{torrent.name}:\n{torrent.num_complete} total numbers of seeders in the swarm.")